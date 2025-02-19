import re
from typing import List
from googlesearch import search
from youtube_transcript_api import YouTubeTranscriptApi


def search_youtube(query: str) -> List[str]:
    """
    Perform a Google search using the provided query and return only valid YouTube video URLs.

    The function appends " youtube" to the query to ensure that the results are YouTube-related.
    Only URLs containing typical video URL patterns are returned.

    Args:
        query: The search query string provided by the user.

    Returns:
        A list of YouTube video URLs (as strings) matching the query.
    """
    query += " youtube"  # Ensure that the search is focused on YouTube videos

    try:
        results = search(query, num_results=10, safe=None, advanced=True)
    except Exception as e:
        print(f"Error performing Google search: {e}")
        return []

    video_urls: List[str] = []
    for result in results:
        url = result.url
        # Include only URLs that are likely to be actual video links
        if ("watch?v=" in url) or ("youtu.be/" in url) or ("youtube.com/shorts/" in url):
            video_urls.append(url)
    return video_urls


def get_video_id_from_url(url: str) -> str:
    """
    Extract the YouTube video ID from a given URL.

    This function uses a regular expression to find the video ID from standard YouTube URLs,
    shortened URLs, and YouTube Shorts URLs.

    Args:
        url: The YouTube video URL.

    Returns:
        The 11-character video ID as a string.

    Raises:
        ValueError: If the URL does not contain a valid YouTube video ID.
    """
    pattern = (
        r"(?:https?://)?(?:www\.)?(?:youtube\.com/(?:watch\?v=|shorts/)|youtu\.be/)"
        r"([a-zA-Z0-9_-]{11})"
    )
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube video URL")


def get_transcript_from_url(url: str) -> str:
    """
    Retrieve the transcript of a YouTube video from the given URL.

    The function first attempts to retrieve an English transcript. If no English transcript is available,
    it will try to fetch the first available transcript and indicate if it is not in English.

    Args:
        url: The YouTube video URL.

    Returns:
        The transcript as a single string, or an error message if retrieval fails.
    """
    try:
        video_id = get_video_id_from_url(url)
    except ValueError as ve:
        return f"Error: {ve}"

    # Attempt to retrieve the English transcript first.
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        text = " ".join(entry["text"] for entry in transcript)
        return text
    except Exception:
        # If the English transcript is not available, try fetching any available transcript.
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript = next(iter(transcript_list))
            text = " ".join(entry["text"] for entry in transcript.fetch())
            if transcript.language_code.lower() != "en":
                text = f"(Transcript is in {transcript.language})\n{text}"
            return text
        except StopIteration:
            return "Error retrieving transcript: No transcripts available."
        except Exception as ex:
            return f"Error retrieving transcript: {ex}"


def main() -> None:
    """
    Main function to run the YouTube transcript search tool.

    Prompts the user for a search query, performs a Google search to find YouTube video URLs,
    and then retrieves and displays the transcript for each video.
    """
    try:
        user_query = input("Enter search query: ")
    except KeyboardInterrupt:
        print("\nUser aborted.")
        return

    youtube_urls = search_youtube(user_query)
    if not youtube_urls:
        print("No video URLs found.")
        return

    for url in youtube_urls:
        print(f"\nProcessing video: {url}")
        transcript = get_transcript_from_url(url)
        print(f"Transcript for {url}:\n{transcript}\n{'-' * 60}")


if __name__ == "__main__":
    main()
