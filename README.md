# Gemini Agent for Google Analytics 4
**Category:** AI & Agents  
**Tech Stack:** Python, Gemini, MCP, Google Analytics 4 API  
**Status:** Complete  
**Thumbnail:** assets/thumbnail.png
## Overview
A Gemini-powered AI agent that connects to Google Analytics 4 via the Model Context Protocol (MCP). Ask natural language questions about your website traffic, get instant reports, and receive AI-summarized insights. Integrates with Claude Desktop or runs standalone.
## Features
- **Natural Language Queries**: "Show me pageviews for the last 30 days"
- **Real-Time Analytics**: Access live GA4 data instantly
- **Period Comparison**: Compare this month vs last month automatically
- **Ranked Reports**: "What are my top 10 pages by traffic?"
- **Account Overview**: List all GA4 properties and accounts
- **MCP Integration**: Works with Claude Desktop, MCP Inspector, or standalone
## Project Structure
```
Gemini-Agent-MCP/
├── src/
│   ├── gemini_client.py          # Main client entry point
│   ├── gemini_server_sample.py   # MCP server implementation
│   ├── gemini_utilities/         # Server connection, encoding, prompts
│   ├── openai_utilities/         # OpenAI client support (optional)
│   ├── tool_sample/              # GA4 report tools
│   └── logfolder/                # Structured logging
├── main.py                       # App launcher
├── pyproject.toml                # Dependencies
└── README.md
```
## Quick Start
### Prerequisites
- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- Google Cloud account with GA4 access
- Gemini API key
### Setup
```bash
git clone https://github.com/Dr-Aniekan-Udo/Gemini-Agent-MCP.git
cd Gemini-Agent-MCP
uv venv && .venv\Scripts\activate
uv sync
1. 
Download Google credentials → rename to credentials.json
2. 
Create src/.env:
GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\credentials.json"
GEMINI_API_KEY="your-key"
Run
# Development
uv run mcp dev src/gemini_server_sample.py
# Standalone client
uv run mcp src/gemini_client.py
# Claude Desktop
uv run mcp install src/gemini_server_sample.py
```
Sample Queries
- 
"Get my traffic report for last week"
- 
"Compare this month's sessions to last month"
- 
"What are my top performing pages?"
- 
"Show real-time active users"
Tech Stack
- 
Framework: LangGraph + MCP
- 
LLM: Google Gemini
- 
Data Source: Google Analytics 4 API
- 
Language: Python 3.10+
- 
Package Manager: uv
Contact
- 
Email: aniekanetimudo+reachout@gmail.com (mailto:aniekanetimudo+reachout@gmail.com)
- 
LinkedIn: Aniekan Etim Udo (https://www.linkedin.com/in/aniekan-etim-udo)
License
MIT
