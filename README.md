# Ask-My-Data
## Description
Ask-My-Data is an innovative, AI-powered data analysis tool that enables users to interact with their datasets using natural language queries. Leveraging Large Language Models (LLMs) integrated via LangChain, the tool dynamically generates SQL queries based on user input, executes them against a SQLite database, and returns results with detailed outputs, including the exact SQL used for transparency. This project evolved through iterative development, addressing challenges like incomplete LLM responses, query extraction errors, and result formatting issues, making it a robust solution for data exploration without requiring deep SQL expertise.

## Purpose
The primary goal of Ask-My-Data is to democratize data analysis by allowing users to ask questions in plain English (e.g., "total revenue by region") and receive actionable insights. It’s designed for quick data exploration from CSV files or SQL databases, serving as a practical tool for business analysts, data enthusiasts, and developers. Additionally, this project serves as a portfolio piece to showcase skills in AI-driven data workflows, LLM integration, and problem-solving during technical interviews. The development process included troubleshooting real-time query generation, handling edge cases like truncated LLM outputs, and ensuring numeric data (e.g., floats) is formatted correctly.

## Technologies
- **Python 3.10+**: Core programming language for the tool.
- **Pandas**: Used to load and manipulate the `sales.csv` dataset into a structured format.
- **SQLAlchemy**: Facilitates database connections and SQL query execution on the `sales.db` SQLite database.
- **LangChain with HuggingFace Endpoint**: Orchestrates the LLM (e.g., Mixtral-8x7B-Instruct-v0.1) to generate SQL queries based on the database schema.
- **python-dotenv**: Manages environment variables, such as the HuggingFace API token.
- **re (Regular Expressions)**: Employed to extract and parse SQL queries from LLM responses, with fixes for incomplete patterns.
- **Future Enhancements**: Planned integration includes OpenAI API for advanced LLM capabilities, Matplotlib for visualizations, Pydantic for structured data validation, Flask for a web-based UI, Docker for deployment, and Chroma for vector search in a Retrieval-Augmented Generation (RAG) system.

## Setup and Usage
### Prerequisites
- **Python 3.10 or higher** installed on your system.
- **Virtual Environment**: Create and activate a virtual environment to isolate dependencies:
  - Windows: `python -m venv ask-my-data-env` followed by `ask-my-data-env\Scripts\activate`.
  - Mac/Linux: `python3 -m venv ask-my-data-env` followed by `source ask-my-data-env/bin/activate`.
- **Install Dependencies**: Run `pip install pandas sqlalchemy langchain langchain-huggingface python-dotenv` to install required packages.
- **Dataset**: The project includes a `sales.csv` file containing sample sales data, which will be loaded into a SQLite database.

### Step-by-Step Instructions
1. **Data Loading**
   - Run `python data_loader.py` to import `sales.csv` into `sales.db`. This script handles data preprocessing and schema creation, ensuring the database is ready for querying. Use `python verify_data_loader.py` to confirm the data loader function works correctly, with debug outputs validating the process.

2. **LLM Setup for SQL Generation**
   - Execute `python llm_setup.py` to test the initial SQL query generation process. This script sets up the LangChain pipeline with the HuggingFace endpoint, using a static prompt to generate SQL based on the database schema (e.g., for "Total revenue"). Screenshots like `llm_setup_static.PNG` document this step.
   - For an unupdated version, use `python llm_setup_unupdated.py` to compare baseline behavior.

3. **Integrate SQL Execution Tool**
   - Run `python sql_executor.py` to execute the generated SQL queries against `sales.db` and retrieve results. This step was refined to handle dynamic queries, with `sql_integration.PNG` showcasing successful executions.

4. **Interactive Terminal-Based Input**
   - Launch the interactive tool with `python llm_setup_interactive.py`. This script combines LLM query generation, SQL execution, and result display in a loop, allowing real-time questioning.
     - **Features**: Users can input questions like "total revenue by region" or "average unit price by item type". The tool extracts SQL from LLM responses, fixes issues (e.g., adding missing `FROM` clauses), and formats results with proper alignment for strings and floats.
     - **Development Highlights**: We addressed challenges such as incomplete LLM outputs (e.g., missing `SUM` or `GROUP BY`), unterminated regex patterns in query extraction, and `AttributeError` with float values in result formatting. Screenshots like `interactive_terminal-based_input.PNG`, `test1.PNG`, and `test2.PNG` capture test runs.
     - **Usage**: Type a question and press Enter. Use "exit" to quit. Debug outputs (e.g., `Debug: Full response`, `Debug: Fixed query`) provide transparency into the process.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
