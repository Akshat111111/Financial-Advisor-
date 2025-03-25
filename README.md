

# Fintech Advisor

## Overview
**Fintech Advisor** is an AI-powered financial analysis tool that leverages a **multi-agent system** to fetch stock market data, analyze financial insights, perform sentiment analysis, and generate comprehensive financial reports.  

The system is built using **CrewAI**, allowing multiple specialized agents to work collaboratively for deep financial insights and structured decision-making.

---

## 🏗 Multi-Agent Workflow
The system follows a structured **multi-agent workflow**, as illustrated in `Workflow.png`. Each agent specializes in a specific task to ensure efficiency and accuracy.  

![Workflow](https://github.com/user-attachments/assets/44288471-8803-40fc-b92f-6aebf5920154)


### 🔹 **Key Agents**
#### 1️⃣ **Financial Agent** (`fin_agents.py`)
- Fetches stock market data using `yfinance`
- Analyzes historical price trends, moving averages, and volatility
- Computes key financial metrics: **CAGR, Sharpe Ratio, Risk Factors**

#### 2️⃣ **News Agent** (`news_template.py`)
- Retrieves real-time financial news related to the stock
- Performs sentiment analysis using **NLP models** (VADER, TextBlob, Transformers)
- Extracts **market trends, keyword insights,** and **investor sentiment**

#### 3️⃣ **Reporter Agent** (`fin_template.py`)
- Aggregates insights from **Financial & News Agents**
- Structures data into **comprehensive financial reports**
- Summarizes key takeaways, risk assessments, and investment opportunities

### 🔹 **Task Orchestration** (`fin_tasks.py`)
- Defines the execution order of tasks for **seamless data flow**
- Ensures **sequential & parallel execution** of AI agents

### 🔹 **Toolset** (`fin_tools.py`)
- Provides additional **AI-driven financial tools**
- Includes **technical indicators, predictive analytics, and trend detection**

---

## 🚀 Features
✅ **AI-Powered Multi-Agent System** – Specialized agents for accurate financial insights  
✅ **Automated Financial Analysis** – Fetches stock data, computes **key performance metrics**  
✅ **Advanced Sentiment Analysis** – Uses NLP to assess **market sentiment & investor mood**  
✅ **Comprehensive Financial Reports** – Summarized **market trends, risk assessment, insights**  
✅ **Interactive Data Visualization** – Uses **Plotly** for visualizing stock trends & analytics  
✅ **Export Functionality** – Download AI-generated reports in **TXT format**  






---



