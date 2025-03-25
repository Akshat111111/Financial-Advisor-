from datetime import datetime
from crewai import Task
from langchain_groq import ChatGroq
from template import fin_template, news_template

class FinTasks:
    def fin_task(self, agent, ticker):
        return Task(
            description=f"""
            Gather an **in-depth financial analysis** for the company {ticker} using reliable financial data tools.
            - Extract **key financial metrics** (P/E ratio, EPS, ROE, Debt-to-Equity, etc.).
            - Analyze **historical stock performance** and trend movements.
            - Compare {ticker}'s **valuation against industry benchmarks**.
            - Identify **financial risks and potential growth drivers**.
            - Format all findings into tables and charts using the **{fin_template}** template.
            """,
            expected_output=f"""Example of a structured financial report for {ticker}:
            <Template>
            {fin_template}
            </Template>
            """,
            agent=agent,
            output_file=f'financial_report_{ticker}.md',
        )

    def news_task(self, agent, ticker):
        return Task(
            description=f"""
            Fetch the **latest 10 financial news articles** about {ticker} using real-time news tools.
            - Categorize each news article as **Bullish, Bearish, or Neutral**.
            - Perform **sentiment analysis** to determine **market perception** of {ticker}.
            - Identify any **major company announcements** or **sector-wide influences**.
            - Provide an **outlook on potential future trends** based on the collected insights.
            - Format the insights in a structured Markdown format using **{news_template}**.
            """,
            expected_output=f"""Example of a structured financial news analysis report for {ticker}:
            <Template>
            {news_template}
            </Template>
            """,
            agent=agent,
            output_file=f'news_report_{ticker}.md',
        )

    def reporter_task(self, context, agent, ticker):
        return Task(
            description=f"""
            Compile a **comprehensive financial report** for {ticker} based on:
            - **Financial Metrics Analysis** from the **Financial Analyst Report**.
            - **News Sentiment Analysis** from the **News Analyst Report**.
            - **Industry and Competitor Comparison** to give broader market context.
            - **Market Sentiment Analysis** based on **recent trends**.
            - **Future Predictions & Risk Analysis** to highlight opportunities & threats.

            📌 **Report Structure:**
            1️⃣ **Executive Summary**  
                - Overview of {ticker}  
                - Key insights & financial health  
                - Summary of recent market trends  
            2️⃣ **Financial Analyst Report (Detailed Breakdown)**  
                - Financial ratios & performance analysis  
                - Profitability & risk assessment  
                - Historical trends & valuation metrics  
            3️⃣ **News & Sentiment Analysis**  
                - Recent headlines categorized (Bullish/Bearish/Neutral)  
                - Sentiment trends impacting stock movements  
                - Key company announcements affecting valuation  
            4️⃣ **Industry & Competitor Analysis**  
                - {ticker} vs Industry Peers  
                - Strengths, Weaknesses, Market Positioning  
            5️⃣ **Future Outlook & Risk Assessment**  
                - Growth Opportunities  
                - Potential Risks & Tailwinds  
                - AI-driven projections & analyst expectations  
            6️⃣ **Data Annex (Tabular Summary)**  
                - Key Financial Data in structured tables  
                - Historical stock performance visualization  
            7️⃣ **Conclusion & Investment Takeaway**  
                - Summary of insights & recommendations  

            The **current date** is {datetime.now().strftime('%Y-%m-%d')}.  
            Generate the full **financial report in Markdown format** for clarity and readability.
            """,
            expected_output=f"""
            **Final Financial Report for {ticker} (Highly Detailed & Structured)**  
            The report should be **low-level, highly informative, and professional**.  
            Use **tables, bullet points, charts, and financial indicators** to provide a comprehensive view.  
            """,
            agent=agent,
            context=context,
            output_file=f'global_report_{ticker}.md',
        )
