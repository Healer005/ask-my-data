# Ask-My-Data
## Description
Ask-My-Data is an innovative, AI-powered data analysis tool that enables users to interact with their datasets using natural language queries. Leveraging Large Language Models (LLMs) integrated via LangChain, the tool dynamically generates SQL queries based on user input, executes them against a SQLite database, and returns results with detailed outputs, including the exact SQL used for transparency. Recent enhancements include visualizations using Matplotlib to graphically represent query results, making it a robust solution for data exploration without requiring deep SQL expertise. The project evolved through iterative development, addressing challenges like incomplete LLM responses, query extraction errors, and result formatting issues.

## Purpose
The primary goal of Ask-My-Data is to democratize data analysis by allowing users to ask questions in plain English (e.g., "total revenue by region") and receive actionable insights, now enhanced with visual aids. It’s designed for quick data exploration from CSV files or SQL databases, serving as a practical tool for business analysts, data enthusiasts, and developers. Additionally, this project serves as a portfolio piece to showcase skills in AI-driven data workflows, LLM integration, and problem-solving during technical interviews. The development process included troubleshooting real-time query generation, handling edge cases like truncated LLM outputs, and ensuring numeric data (e.g., floats) is formatted correctly, with visualizations as the latest milestone.

## Technologies
- **Python 3.10+**: Core programming language for the tool.
- **Pandas**: Used to load and manipulate the `sales.csv` dataset into a structured format.
- **SQLAlchemy**: Facilitates database connections and SQL query execution on the `sales.db` SQLite database.
- **LangChain with HuggingFace Endpoint**: Orchestrates the LLM (e.g., Mixtral-8x7B-Instruct-v0.1) to generate SQL queries based on the database schema.
- **python-dotenv**: Manages environment variables, such as the HuggingFace API token.
- **re (Regular Expressions)**: Employed to extract and parse SQL queries from LLM responses, with fixes for incomplete patterns.
- **Matplotlib**: Added for generating visualizations (e.g., bar charts) of query results.
- **Future Enhancements**: Planned integration includes OpenAI API for advanced LLM capabilities, Pydantic for structured data validation, Flask for a web-based UI, Docker for deployment, and Chroma for vector search in a Retrieval-Augmented Generation (RAG) system.

## Setup and Usage
### Prerequisites
- **Python 3.10 or higher** installed on your system.
- **Virtual Environment**: Create and activate a virtual environment to isolate dependencies:
  - Windows: `python -m venv ask-my-data-env` followed by `ask-my-data-env\Scripts\activate`.
  - Mac/Linux: `python3 -m venv ask-my-data-env` followed by `source ask-my-data-env/bin/activate`.
- **Install Dependencies**: Run `pip install pandas sqlalchemy langchain langchain-huggingface python-dotenv matplotlib` to install required packages.
- **Dataset**: The project includes a `sales.csv` file containing sample sales data, which will be loaded into a SQLite database.

### Step-by-Step Instructions
1. **Data Loading**
   - Run `python data_loader.py` to import `sales.csv` into `sales.db`. This script handles data preprocessing and schema creation, ensuring the database is ready for querying. Use `python verify_data_loader.py` to confirm the data loader function works correctly, with debug outputs validating the process.
   - <img width="1089" height="511" alt="image" src="https://github.com/user-attachments/assets/b53b49cc-845f-4279-b256-f4e07801f3a1" />

2. **LLM Setup for SQL Generation**
   - Execute `python llm_setup.py` to test the initial SQL query generation process. This script sets up the LangChain pipeline with the HuggingFace endpoint, using a static prompt to generate SQL based on the database schema (e.g., for "Total revenue"). Screenshots like `llm_setup_static.PNG` document this step.
   - For an unupdated version, use `python llm_setup_unupdated.py` to compare baseline behavior.

3. **Integrate SQL Execution Tool**
   - Run `python sql_executor.py` to execute the generated SQL queries against `sales.db` and retrieve results. This step was refined to handle dynamic queries, with `sql_integration.PNG` showcasing successful executions.
   - <img width="1087" height="428" alt="sql_integration" src="https://github.com/user-attachments/assets/ae11af75-8b95-45b2-b0f5-921b989d0198" />

4. **Interactive Terminal-Based Input**
   - Launch the interactive tool with `python llm_setup_interactive.py`. This script combines LLM query generation, SQL execution, and result display in a loop, allowing real-time questioning.
     - **Features**: Users can input questions like "total revenue by region" or "average unit price by item type". The tool extracts SQL from LLM responses, fixes issues (e.g., adding missing `FROM` clauses), and formats results with proper alignment for strings and floats.
     - **Development Highlights**: We addressed challenges such as incomplete LLM outputs (e.g., missing `SUM` or `GROUP BY`), unterminated regex patterns in query extraction, and `AttributeError` with float values in result formatting.
     - **Usage**: Type a question and press Enter. Use "exit" to quit. Debug outputs (e.g., `Debug: Full response`, `Debug: Fixed query`) provide transparency into the process.
   - <img width="1908" height="920" alt="interactive_terminal-based_input" src="https://github.com/user-attachments/assets/a60a95b6-5076-4fbb-b396-d0bff2cd5bb1" />

5. **Add Visualizations**
   - The latest enhancement adds Matplotlib visualizations to `llm_setup_interactive.py`. Run the script and input grouped queries (e.g., "total revenue by sales channel") to see bar charts representing the data.
     - **Features**: Visualizations automatically generate for two-column results with numeric values (e.g., `Region` vs. `Total_Revenue`), using dynamic labels from query headers.
     - **Development Highlights**: The visualization logic was designed to handle diverse questions, detecting numeric data without assuming specific column names, building on fixes for query extraction and result formatting.
     - **Usage**: After results are displayed, a chart window will appear if the query returns grouped numeric data.
   - <img width="1534" height="600" alt="eg 1" src="https://github.com/user-attachments/assets/a6d75af9-5789-4c6f-aaf5-70f1d3027d57" />
   - <img width="1592" height="607" alt="eg 2" src="https://github.com/user-attachments/assets/ea92b3f0-ef43-4cc1-a531-5b89324c7413" />

## Query Validation and Cross-Verification
- The accuracy of the generated SQL queries has been validated by cross-checking with MySQL Workbench. Users can copy the "Generated SQL" output from the interactive tool, execute it in MySQL Workbench after connecting to a compatible database (e.g., exporting `sales.db` to MySQL), and compare the results with the tool’s output.
- **Testing Process**: For example, the query `SELECT `Sales Channel`, SUM(`Total Revenue`) AS Total_Revenue FROM sales GROUP BY `Sales Channel`;` was tested, confirming matching row counts and aggregated values.
- **Development Insight**: This step ensured the tool’s reliability, identifying and resolving discrepancies (e.g., incomplete queries) during development.
- <img width="1920" height="1030" alt="test_1" src="https://github.com/user-attachments/assets/5d9ec517-3388-40e1-a52c-f4019151a523" />
- <img width="619" height="471" alt="cross_verification" src="https://github.com/user-attachments/assets/34520069-bcb4-4453-ae4a-a8595ae2c414" />

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
