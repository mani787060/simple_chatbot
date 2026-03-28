# Gemini Terminal Chatbot
[![Google AI](https://img.shields.io/badge/API-Google%20Gemini-4285F4)](https://ai.google.dev/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)

## 💬 Project Overview
This repository contains a lightweight, **Terminal-based AI Chatbot** powered by Google’s Gemini Pro model. The project focuses on the core logic of stateful AI interactions, utilizing the Gemini SDK's native `ChatSession` to maintain context across multiple turns without needing a complex web UI or frontend framework.

---

## 🛠️ Key Technical Implementations

### 1. Native Session Management
* **`start_chat()` Engine:** Instead of manually managing an array of message objects, this implementation uses Gemini’s built-in session handler to track conversation flow.
* **Persistent Context:** The chatbot remembers previous user inputs within the same session, allowing for complex, multi-step reasoning.

### 2. Command-Line Interface (CLI)
* **Infinite Loop Architecture:** A robust `while True` loop that handles real-time user input and AI response streaming.
* **Session Controls:** Integrated commands (like `exit` or `quit`) to allow users to terminate the script cleanly.

### 3. Developer Best Practices
* **Environment Security:** Utilizes `.env` files and `python-dotenv` to keep API keys private and out of version control.
* **Clean Output Formatting:** Organized terminal print statements to distinguish between User and Assistant roles.

---

## 💻 Tech Stack
* **Language:** Python 3.9+
* **AI Model:** Google Gemini Pro
* **Library:** `google-generativeai`
* **Environment Management:** `python-dotenv`


