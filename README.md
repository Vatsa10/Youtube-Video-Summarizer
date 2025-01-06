
# Summarize Text From YouTube or Website

This project leverages LangChain and the Groq language model to summarize content from YouTube videos and generic websites. Users can input a URL, and the application extracts content, processes it, and provides a concise summary.

---

## Features

- **YouTube Transcript Summarization**: Extracts captions or transcripts from YouTube videos using the `youtube-transcript-api`.
- **Advanced LLM Integration**: Uses the `llama-3.1-70b-versatile` model via Groq for generating summaries.
- **Streamlit UI**: Provides an intuitive and user-friendly interface for inputting URLs and viewing summaries.

---

## Prerequisites

### Required Python Libraries

Ensure you have the following Python libraries installed:

- `streamlit`
- `langchain`
- `langchain_groq`
- `langchain_community`
- `youtube-transcript-api`
- `urllib3`

You can install them using:

```bash
pip install streamlit langchain langchain_groq langchain_community youtube-transcript-api urllib3
```

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Vatsa10/Youtube-Video-Summarizer/
   cd Youtube-Video-Summarizer
   ```

2. Set up your Groq API Key:

   - Add your Groq API Key to the environment variable `GROQ_API_KEY` or enter it in the Streamlit sidebar.

3. Run the Streamlit application:

   ```bash
   streamlit run main.py
   ```

4. Open the application in your browser at `http://localhost:8501`.

---

## Usage

1. Enter your **Groq API Key** in the sidebar.
2. Input a valid URL in the main text field. This can be a YouTube video or any website URL.
3. Click on the **"Summarize the Content from YT or Website"** button.
4. View the generated summary in the output area.

---

## Error Handling

- **Invalid URLs**: The application verifies the URL format and prompts users if the URL is incorrect.
- **YouTube Transcript Issues**: If the transcript is unavailable, an appropriate error message is displayed.
- **Empty Content**: The application ensures content is extracted before attempting summarization.

---

## File Structure

- `YTB.py`: Main Streamlit application script.
- `requirements.txt`: Dependencies for the project.

---

## Example

### Input

YouTube URL: `https://www.youtube.com/watch?v=Gjnup-PuquQ`

### Output

A concise 300-word summary of the video content.
![image](https://github.com/Vatsa10/Youtube-Video-Summarizer/blob/main/Output%20Photo%20.png)
**You can also check out the whole video here https://github.com/Vatsa10/Youtube-Video-Summarizer/blob/main/Output%20Video.mp4**
---

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss your proposed changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [LangChain](https://langchain.com/) for providing the summarization chain.
- [Streamlit](https://streamlit.io/) for the interactive UI.
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for transcript extraction.
- [Groq](https://groq.com/) for the advanced LLM.

