# YouTube Transcript Search Tool

A simple Python tool that searches for YouTube videos using Google and retrieves the transcripts for each video. The tool attempts to fetch an English transcript by default and falls back to any available transcript if English is not available.

## Features

- **Google Search Integration:** Automatically appends "youtube" to the search query to focus on YouTube results.
- **URL Filtering:** Filters out non-video URLs, ensuring only valid YouTube video links are processed.
- **Transcript Retrieval:** Fetches transcripts using the [youtube_transcript_api](https://github.com/jdepoix/youtube-transcript-api).
- **Error Handling:** Provides clear error messages if transcripts cannot be retrieved.
- **Terminal-Friendly:** Designed to run smoothly in a terminal environment.

## Requirements

- Python 3.6+
- [googlesearch-python](https://pypi.org/project/googlesearch-python/) (or a similar package providing the `search` function)
- [youtube_transcript_api](https://pypi.org/project/youtube-transcript-api/)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the Required Packages:**

   ```bash
   pip install googlesearch-python youtube-transcript-api
   ```

## Usage

1. Run the script in your terminal:

   ```bash
   python transcript_search.py
   ```

2. When prompted, enter your search query. For example:

   ```
   Enter search query: your search term here
   ```

3. The tool will display the YouTube video URLs found and print the transcript for each video.

## Example Output

```
Enter search query: inspirational speech

Processing video: https://www.youtube.com/watch?v=EXAMPLE_ID
Transcript for https://www.youtube.com/watch?v=EXAMPLE_ID:
This is an example transcript of the YouTube video...
------------------------------------------------------------
```


## Acknowledgements

- [youtube_transcript_api](https://github.com/jdepoix/youtube-transcript-api)
- [googlesearch-python](https://pypi.org/project/googlesearch-python/)
