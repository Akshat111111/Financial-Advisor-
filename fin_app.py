import streamlit as st
import sys
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from crewai import Crew, Process
from fin_agents import FinAgents, StreamToExpander
from fin_tasks import FinTasks
import tempfile
import os

st.set_page_config(page_icon="📝", page_title="ZeeFinReporter", layout="wide")


class FinancialCrew:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.output_placeholder = st.empty()

    def run(self):
        agents = FinAgents()
        tasks = FinTasks()

        fin_agent = agents.fin_agent()
        news_agent = agents.news_agent()
        reporter_agent = agents.reporter_agent()

        fin_task = tasks.fin_task(fin_agent, self.ticker, self.start_date, self.end_date)
        news_task = tasks.news_task(news_agent, self.ticker)
        reporter_task = tasks.reporter_task([fin_task, news_task], reporter_agent, self.ticker)

        crew = Crew(
            agents=[fin_agent, news_agent, reporter_agent],
            tasks=[fin_task, news_task, reporter_task],
            process=Process.sequential,
            full_output=True,
            share_crew=False,
            verbose=True
        )

        result = crew.kickoff()
        self.output_placeholder.markdown(result)
        return result


def fetch_stock_data(ticker, start_date, end_date):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(start=start_date, end=end_date)
        return df
    except Exception as e:
        st.error(f"Error fetching stock data: {e}")
        return None


def generate_sentiment_score(news_articles):
    # Placeholder for sentiment analysis logic (can integrate NLP models like VADER, TextBlob, etc.)
    return round(sum([article["sentiment_score"] for article in news_articles]) / len(news_articles), 2)


def export_report(result, ticker):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(f"📊 {ticker} Financial Report\n\n".encode())
        temp_file.write(result["final_output"].encode())
        file_path = temp_file.name

    st.download_button(
        label="📥 Download Report",
        data=open(file_path, "rb").read(),
        file_name=f"{ticker}_Financial_Report.txt",
        mime="text/plain"
    )
    os.remove(file_path)


st.header("🏛️ Financial Reporter :orange[Ai]gent 📊", divider="orange")

with st.sidebar:
    st.caption("Financial Agent")
    st.markdown(
        """
        # 🏛️ Financial Reporter 📈
        1. Enter a stock ticker
        2. Select date range
        3. Get insights, news, and sentiment analysis
        4. Generate a detailed financial report
        5. Export report in TXT format
        """
    )
    st.divider()
    

st.session_state.plan_pressed = False

ticker = st.text_input("📈 Enter Stock Ticker:", placeholder="AAPL, TSLA...")

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("📅 Start Date", datetime.now() - timedelta(days=365))
with col2:
    end_date = st.date_input("📅 End Date", datetime.now())

if ticker:
    stock_data = fetch_stock_data(ticker, start_date, end_date)

    if stock_data is not None and not stock_data.empty:
        st.subheader(f"📊 {ticker} Stock Performance", anchor=False, divider="rainbow")
        fig = px.line(stock_data, x=stock_data.index, y="Close", title=f"{ticker} Stock Price Over Time")
        st.plotly_chart(fig, use_container_width=True)

        if st.button("💫 Generate Financial Report", use_container_width=True, key="generate"):
            with st.spinner("🤖 Agents analyzing the data..."):
                with st.status("🤖 **Generating Report...**", state="running", expanded=True) as status:
                    with st.container(height=300, border=False):
                        sys.stdout = StreamToExpander(st)
                        financial_crew = FinancialCrew(ticker, start_date, end_date)
                        result = financial_crew.run()

                    status.update(label="✅ Financial Report Generated! 📊", state="complete", expanded=False)

            st.subheader(f"📊 {ticker} Financial Report 📰", anchor=False, divider="rainbow")
            st.markdown(result["final_output"])
            st.divider()

            st.json(result['usage_metrics'])
            st.divider()

            for i, task in enumerate(result['tasks_outputs']):
                with st.expander(f"Agent Report {i+1} :", expanded=False):
                    st.markdown(task)

            export_report(result, ticker)
            st.divider()
    else:
        st.warning("⚠️ No stock data available for the selected date range. Please try again.")







