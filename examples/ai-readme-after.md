<!--
This file is the ASD-STE100 rewrite of `ai-slop-readme-before.md`.
Source: https://github.com/typhonshambo/ai-styleguide (README.md), MIT License.
The personal names and the contact details are replaced with generic text.
-->

<img src='https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlebard&logoColor=fff'>

# Code Style Guide Tool with the Gemini API

## Project overview

This project makes a tool that keeps the code style of a project the same.
The tool uses the Gemini API. It writes a style guide for one user.
The style guide agrees with the code that the user writes.
The tool also sends feedback and gives suggestions while the user writes code.

## Problem

Different code styles in one project make the code difficult to read.
They also make the code difficult to maintain.
Many style guides are fixed. They do not change for one user or for one project.

## Solution

The tool does these three functions:

1.  **Analysis:** the tool reads the code of the user. It finds the code patterns of the user.
2.  **Style guide:** the tool writes a style guide. The style guide agrees with the code of the user and with the usual best practice.
3.  **Feedback:** the tool sends feedback and suggestions to the code editor.

## Demo
https://github.com/typhonshambo/ai-styleguide/assets/54593764/852f3357-a0b4-4313-9096-6d4ea19b2394

[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://ai-styleguide.streamlit.app)


## Setup
 > This procedure is for the VS Code extension.
1. Start the backend.
```bash
pip3 install -r requirements.txt
python3 server.py
```
2. Compile the extension on your machine.
```bash
npm install
npm run compile
```
3. Start the debugger. The debugger opens a VS Code workspace that has the extension. Do a test of the extension in this workspace.

## Functions

*   **Style guide for one user:** the tool reads the code, finds the usual patterns, and writes a style guide.
*   **Feedback:** the tool gives suggestions about the format and the style while the user writes code.
*   **Editor integration:** the tool operates in usual code editors.
*   **Changes by the user:** the user can change the style guide for the needs of one project.
*   **Adaptation:** the tool adapts to the code style of the user with time.

## Technical approach

*   **Code analysis:** the tool uses Natural Language Processing (NLP) methods. These methods include parsers, abstract syntax trees (ASTs), and transformer models such as CodeBERT.
*   **Gemini API:** the tool sends the code to the Gemini API. The Gemini API gives the feedback and the suggestions.
*   **Flask backend:** the backend uses Flask. The backend receives the API requests, processes the data, and communicates with Gemini.
*   **Streamlit frontend:** the frontend uses Streamlit. In the frontend, the user gives the code, looks at the style guide, changes the style guide, and receives the feedback.


## Team

*   **Maintainer:** has experience with Python, C, SQL, and data science tools.

## Contribution

You can help with this project. Look at the open issues in the
[GitHub repository](https://github.com/your-repo). Then assign an issue to
yourself.

## Contact
Send your questions to the maintainer.
