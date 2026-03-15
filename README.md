# Ask-My-Data

## 📌 Description
**Ask-My-Data** is an innovative, AI-powered data analysis tool that allows users to interact with their datasets using natural language queries.  
The tool leverages **Large Language Models (LLMs)** via **LangChain**, generates SQL queries, executes them against a local **SQLite database**, and visualizes results with **Matplotlib**.  

Think of it as asking questions in English — and getting back **SQL queries, answers, and charts** automatically.  

---

## ⚡ Features
- 🧠 Convert natural language queries into **SQL**  
- 📊 Visualize results with **Matplotlib**  
- 💾 Validate against **SQLite database**  
- 🔗 Powered by **LangChain + Python**  
- 📷 Includes verification screenshots of queries and results  

---

## 📂 Project Structure
```
Ask-My-Data/
│
├── README.md                 # Project overview
├── LICENSE                   # License file
├── requirements.txt          # Python dependencies
│
├── data/                     # Datasets
│   ├── sales.csv
│   └── sales.db
│
├── src/                      # Source code
│   ├── data_loader.py
│   ├── verify_data_loader.py
│   ├── sql_executor.py
│   ├── llm_setup_interactive.py
│   ├── llm_setup_static.py
│   └── llm_setup_unupdated.py
│
├── results/                  # Outputs & screenshots
│   ├── cross_verification.PNG
│   ├── sql_integration.PNG
│   ├── test1.PNG
│   ├── total_revenue_by_region.PNG
│   └── ...
│
│
```

---

## 🛠️ Installation

Clone the repo:
```bash
git clone https://github.com/your-username/Ask-My-Data.git
cd Ask-My-Data
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Load Dataset
```bash
python src/data_loader.py
```

### 2. Run LLM Setup
- Interactive Mode:
```bash
python src/llm_setup_interactive.py
```
- Static Mode:
```bash
python src/llm_setup_static.py
```

### 3. Execute SQL Queries
```bash
python src/sql_executor.py
```

---

## 📊 Examples

**Query:**  
👉 "Show me the total revenue by region"  

**Generated SQL:**  
```sql
SELECT region, SUM(revenue) as total_revenue 
FROM sales 
GROUP BY region;
```

**Visualization:**  
[Total Revenue by Region]
<img width="1000" height="600" alt="total_revenue_by_region" src="https://github.com/user-attachments/assets/886ca81c-275f-4c9e-bc84-d2784d015776" />

---

## ✅ Screenshots & Results
- SQL integration test
<img width="1087" height="428" alt="sql_integration" src="https://github.com/user-attachments/assets/fa5a6941-d1ab-4bcc-a598-e884ad5d4f7c" />
- Interactive terminal-based input
<img width="1908" height="920" alt="interactive_terminal-based_input" src="https://github.com/user-attachments/assets/ed504113-a9af-4ced-ac89-8fe4c044a6ce" />
- Tests
<img width="1920" height="1030" alt="test_1" src="https://github.com/user-attachments/assets/3ee20600-6e09-4c15-a730-b331e949f181" />
<img width="1920" height="1030" alt="test_2" src="https://github.com/user-attachments/assets/52c5e965-632c-4a2d-b5fe-f2a0ce3b1656" />
<img width="1920" height="1030" alt="test_3" src="https://github.com/user-attachments/assets/564d21b4-1abf-4c91-9e19-923def9e3975" />
- Visualization Examples



---

## 📌 Future Improvements
- Add **PostgreSQL/MySQL** backend support  
- Enable **interactive web dashboard (Streamlit/Flask)**  
- Integrate **LLM fine-tuning** for better query accuracy  

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.  

---

## 📜 License
This project is licensed under the **MIT License**.  
