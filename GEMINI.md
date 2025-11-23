Project Overview

This project is an AI-powered PDF Study Assistant built using OpenAgents SDK, Gemini , Streamlit, PyPDF, and Context7 MCP.
The system allows users to upload any PDF, automatically extract text, and generate two core outputs:

1. PDF Summarizer

User uploads a PDF through the Streamlit interface.

Text is extracted using PyPDF.

The agent (powered by Gemini ) produces a clean, concise summary.

Summary is displayed in a simple UI component (card, block, or container).

2. Quiz Generator

After summarization, the user clicks Create Quiz.

The agent reads the original PDF text (not the summary).

It generates a quiz in either:

Multiple-choice format, or

Mixed question styles (MCQs, True/False, Fill-in-the-blank).

Technology Stack

OpenAgents SDK — runs the agent logic

Gemini Model  — provides AI reasoning

Streamlit — simple UI for upload, summary, and quiz

PyPDF — extracts text from PDF files

Context7 MCP — provides additional tools for the agent

Goal

Create a minimal but functional AI agent that supports learning by summarizing academic PDFs and auto generating quizzes base on orignal pdf.