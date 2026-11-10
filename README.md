# Build Simple AI Agent

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/LangChain-Agents-00A9F0?logo=langchain&logoColor=white" alt="LangChain" />
  <img src="https://img.shields.io/badge/Model-Claude-ff8f00?logo=anthropic&logoColor=white" alt="Claude" />
</p>

A lightweight research assistant built with Python and LangChain. The agent uses Claude as its reasoning engine, can search the web and Wikipedia, and saves findings to a local output file for later review.

## Overview
This project demonstrates how to build a minimal AI agent with tool calling. The application accepts a user query, decides which tools to use, gathers supporting information, and returns a structured response. It is intentionally simple and beginner-friendly while showing the core ideas behind agent-based workflows.

## Features
- CLI-based interaction for research queries
- Claude-powered reasoning and response generation
- Web search using DuckDuckGo
- Wikipedia lookup support
- Structured output parsing with Pydantic
- Automatic saving of research output to a text file
- Lightweight, easy-to-understand architecture

## Tech Stack
- Python
- LangChain
- Anthropic Claude
- DuckDuckGo Search
- Wikipedia API
- Pydantic
- python-dotenv

## Project Structure
```text
build-simple-ai-agent/
├── README.md
├── requriements.txt
├── research_output.txt
├── src/
│   ├── main.py
│   └── tools.py
├── .env.example
└── .gitignore
```

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/build-simple-ai-agent.git
cd build-simple-ai-agent
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requriements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

### 5. Run the application
```bash
python src/main.py
```

### 6. Ask a question
```text
What can I help you research?
```

## How It Works
- `src/main.py` initializes the LLM and defines the agent workflow.
- `src/tools.py` contains the custom tools for web search, Wikipedia lookup, and file saving.
- The agent uses tool calling to gather relevant information before composing a final response.
- The generated research result is appended to `research_output.txt`.

## Example Workflow
1. A user enters a research prompt.
2. The AI decides whether to use web search or Wikipedia.
3. The agent retrieves supporting information from the selected tools.
4. A structured answer is generated using the model response parser.
5. Results are saved to `research_output.txt`.

## Architecture
```text
User Query
   ↓
Claude LLM
   ↓
Tool-calling Agent
   ├── DuckDuckGo Search
   ├── Wikipedia API
   └── Save to File
   ↓
Structured Output
```

## Challenges Faced
- Configuring LangChain agent tool calling correctly
- Integrating external search and Wikipedia tools
- Parsing structured LLM responses with Pydantic
- Managing environment variables and API access securely

## Solutions
- Used a tool-calling agent pattern instead of a simple prompt-only setup
- Wrapped external search and wiki functionality in reusable tools
- Parsed structured responses with `PydanticOutputParser`
- Stored API configuration in `.env` with `python-dotenv`

## Notes
This project is intentionally minimal and educational. It is designed to help beginners understand how an LLM agent can use tools to gather information and produce more useful, grounded responses.

## References
- Tech With Tim — "Build an AI Agent From Scratch in Python - Tutorial for Beginners"
  - https://youtu.be/bTMPwUgLZf0?si=1gNpxbU35PKwY5GF

## License
This project is provided for educational purposes and is not currently licensed for commercial distribution.


