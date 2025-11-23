import streamlit as st
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled 
from openai import  OpenAI
from dotenv import load_dotenv
import os
import PyPDF2


# Disable tracing for performance optimization
set_tracing_disabled(True)

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the Gemini client
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Configure the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

# Create the agents
summarizer_agent = Agent(
    name="PDF Summarizer",
    instructions="You are a helpful assistant that summarizes PDF documents.",
    model=model
)
quiz_generator = Agent(
    name="Quiz Generator",
    instructions="You are a helpful assistant that generates quizzes based on original PDF documents.",
    model=model
)


def extract_text_from_pdf(file):
    """Extracts text from a PDF file."""
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def main():
    """Main function for the Streamlit app."""
    st.set_page_config(page_title="PDF Study Assistant", page_icon=":books:")
    st.title("PDF Study Assistant")

    with st.sidebar:
        st.header("Upload PDF")
        uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

        if uploaded_file is not None:
            st.success("File uploaded successfully!")
            if st.button("Summarize"):
                st.session_state.action = "summarize"
            if st.button("Generate Quiz"):
                st.session_state.action = "quiz"

    if "action" in st.session_state and uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        if st.session_state.action == "summarize":
            with st.spinner("Summarizing..."):
                # Use Runner.run_sync() directly
                summary_result = Runner.run_sync(summarizer_agent, f"Summarize the following text:\n\n{pdf_text}")
                summary = summary_result.final_output
                st.header("Summary")
                st.write(summary)
        elif st.session_state.action == "quiz":
            with st.spinner("Generating Quiz..."):
                # Use Runner.run_sync() directly
                quiz_result = Runner.run_sync(quiz_generator, f"Generate a quiz from the following text:\n\n{pdf_text}")
                quiz = quiz_result.final_output
                st.header("Quiz")
                st.write(quiz)

if __name__ == "__main__":
    main()