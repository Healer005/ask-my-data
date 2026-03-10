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
All verification screenshots are available inside the `results/` folder.  
They include:  
- SQL integration test  
- Query validation outputs  
- Revenue by region & sales channel  
- Order priority analysis
   
<img width="1087" height="428" alt="sql_integration" src="https://github.com/user-attachments/assets/fa5a6941-d1ab-4bcc-a598-e884ad5d4f7c" />

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
