import os
import streamlit as st  # type: ignore
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader
from youtube_transcript_api import YouTubeTranscriptApi # type: ignore
from langchain.schema import Document

# Streamlit page setup
st.set_page_config(page_title="Summarize Text From YT or Website", page_icon="")
st.title("Summarize Text From YT or Website")
st.subheader('Summarize URL')

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

# Check if API key is provided
if not groq_api_key.strip():
    st.error("Please enter a valid Groq API Key in the sidebar.")
    st.stop()

# Initialize the LLM
llm = ChatGroq(model="llama-3.1-70b-versatile", groq_api_key=groq_api_key)

# Prompt template
prompt_template = """
Provide a summary of the following content in 300 words:
Content: {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

def fetch_youtube_transcript(video_url):
    """Fetches transcript from YouTube using the youtube-transcript-api."""
    try:
        video_id = video_url.split('v=')[-1].split('&')[0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item['text'] for item in transcript])
    except Exception as e:
        return f"Error: {e}"

generic_url = st.text_input("Enter a YouTube or Website URL", label_visibility="collapsed")

if st.button("Summarize the Content from YT or Website"):
    if not generic_url.strip():
        st.error("Please provide a URL to get started.")
    else:
        try:
            with st.spinner("Processing..."):
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    # Attempt to fetch YouTube captions/transcript
                    transcript = fetch_youtube_transcript(generic_url)
                    if "Error" in transcript:
                        st.error(transcript)
                        st.stop()
                    docs = [Document(page_content=transcript, metadata={"source": generic_url})]
                else:
                    # Load content from a generic website
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=True,
                        headers={"User-Agent": "Mozilla/5.0"}
                    )
                    docs = loader.load()

                # Check if content is available
                if not docs or not docs[0].page_content.strip():
                    st.error("No content extracted. Please provide a valid URL with accessible content.")
                    st.stop()

                # Summarize the content
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.invoke({"input_documents": docs})

                st.success("Summary:")
                st.write(output_summary)
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
