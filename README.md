# Ask-My-Data

## Description
Ask-My-Data is an intelligent data analysis tool powered by LLMs (Large Language Models) that allows users to chat with their datasets in natural language. It interprets queries, generates SQL, executes them on the data, and returns answers with visualizations and the exact SQL used for transparency.

## Purpose
This tool is designed to make data analysis accessible without deep SQL or programming knowledge. It's ideal for data exploration, quick insights from CSVs or SQL databases, and demonstrating skills in AI-driven data workflows. It's built as a portfolio project for interviews, showcasing integration of LLMs with data tools.

## Technologies
- Python 3.10+
- Pandas (for data loading and manipulation)
- SQLAlchemy (for database connections and operations)
- LangChain (for LLM orchestration)
- Future steps will include: OpenAI API (for LLM), Matplotlib (for visualizations), Pydantic (for structured outputs), Flask (for UI), Docker (for deployment), and Chroma (for vector search in RAG).
  
## Setup and Usage
### Prerequisites
- Install Python 3.10+.
- Create a virtual environment: `python -m venv ask-my-data-env` and activate it with `ask-my-data-env\Scripts\activate` (Windows).
- Install packages: `pip install pandas sqlalchemy langchain langchain-huggingface python-dotenv`.
- The dataset `sales.csv` is included.
- Create a `.env` file in the project root with your Hugging Face API token: `HUGGINGFACEHUB_API_TOKEN=your_actual_hf_token_here` (replace with your token from https://huggingface.co/settings/tokens).
### Step 1: Data Loading
- Run `python data_loader.py` to load `sales.csv` into `sales.db` (SQLite).
### Step 2: LLM Setup for SQL Generation
- Configure `llm_setup.py` to use `mistralai/Mixtral-8x7B-Instruct-v0.1` with `ChatHuggingFace` to generate SQL queries from natural language prompts.
- Instructions:
  1. Ensure `llm_setup.py` is updated with the provided code.
  2. Run `python llm_setup.py` to generate a SQL query (e.g., for "Total revenue by region").
  - Note: The script extracts the SQL query from the model’s response. If explanatory text appears, the regex in `extract_sql_query` may need adjustment.
  - Troubleshooting: If a `StopIteration` or `ValueError` occurs, verify the model’s free tier availability or switch to a supported alternative (e.g., `gpt2`).
  
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
