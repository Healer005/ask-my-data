# Ask-My-Data

## Description
Ask-My-Data is an intelligent data analysis tool powered by LLMs (Large Language Models) that allows users to chat with their datasets in natural language. It interprets queries, generates SQL, executes them on the data, and returns answers with visualizations and the exact SQL used for transparency.

## Purpose
This tool is designed to make data analysis accessible without deep SQL or programming knowledge. It's ideal for data exploration, quick insights from CSVs or SQL databases, and demonstrating skills in AI-driven data workflows. It's built as a portfolio project for interviews, showcasing integration of LLMs with data tools.

## Technologies
- Python 3.10+
- Pandas (for data loading and manipulation)
- SQLAlchemy (for database connections and operations)
- Future steps will include: LangChain (for LLM orchestration), OpenAI API (for LLM), Matplotlib (for visualizations), Pydantic (for structured outputs), Flask (for UI), Docker (for deployment), and Chroma (for vector search in RAG).

## Setup and Usage
### Prerequisites
- Install Python 3.10+.
- Create a virtual environment: `python -m venv ask-my-data-env` and activate it with `ask-my-data-env\Scripts\activate` (Windows).
- Install packages: `pip install pandas sqlalchemy`.
- The dataset `sales.csv` is included.

### Step 1: Data Loading
Run `python data_loader.py` to load `sales.csv` into `sales.db` (SQLite).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
