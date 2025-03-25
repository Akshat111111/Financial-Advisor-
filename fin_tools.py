from crewai_tools import tool
from langchain_community.tools import DuckDuckGoSearchResults
import yfinance as yf
import pandas as pd
import json

class SearchTool:

    @tool("search web tool")
    def search_web_tool(query):
        """
        Query the internet for the latest financial news related to a stock ticker and return up-to-date relevant results.
        """
        try:
            search_tool = DuckDuckGoSearchResults(backend="news", num_results=10, verbose=True)
            results = search_tool.run(query)
            return json.dumps(results, indent=2)  # Return formatted JSON results
        except Exception as e:
            return f"Error retrieving news: {str(e)}"

    @tool("financial data tool")
    def financial_data_tool(ticker):
        """
        Retrieve an extensive set of financial metrics, statements, and stock-related news for a given stock ticker.
        """
        try:
            stock = yf.Ticker(ticker)
            stock_info = stock.info

            document = f"📊 **Financial Data for {ticker}**\n"
            document += f"**Company Name:** {stock_info.get('longName', 'N/A')}\n"
            document += f"**Sector:** {stock_info.get('sector', 'N/A')} | **Industry:** {stock_info.get('industry', 'N/A')}\n"
            document += f"**Market Cap:** {stock_info.get('marketCap', 'N/A')} ₹\n"
            document += f"**Current Price:** {stock_info.get('currentPrice', 'N/A')} ₹\n"

            # Extract key financial ratios
            financial_ratios = {
                "P/E Ratio": stock_info.get("trailingPE", "N/A"),
                "Forward P/E": stock_info.get("forwardPE", "N/A"),
                "Return on Equity (ROE)": stock_info.get("returnOnEquity", "N/A"),
                "Return on Assets (ROA)": stock_info.get("returnOnAssets", "N/A"),
                "Debt to Equity Ratio": stock_info.get("debtToEquity", "N/A"),
                "Profit Margins": stock_info.get("profitMargins", "N/A"),
                "EBITDA Margins": stock_info.get("ebitdaMargins", "N/A"),
                "Gross Margins": stock_info.get("grossMargins", "N/A")
            }

            document += "\n## 📉 **Financial Ratios**\n"
            for key, value in financial_ratios.items():
                document += f"- **{key}:** {value}\n"

            # Stock News
            news = stock.news
            document += "\n## 📰 **Latest Stock News**\n"
            if news:
                for i, item in enumerate(news[:5]):  # Limit to top 5 news articles
                    document += f"{i+1}. **{item['title']}**\n"
                    document += f"   - Publisher: {item['publisher']}\n"
                    document += f"   - Related Tickers: {item['relatedTickers']}\n"
            else:
                document += "No news available for this stock.\n"

            return document
        except Exception as e:
            return f"Error retrieving financial data: {str(e)}"

    @tool("financial statement tool")
    def financial_statement_tool(ticker):
        """
        Retrieve balance sheet, cash flow statement, and income statement for a given stock ticker with multi-year data.
        """
        try:
            stock = yf.Ticker(ticker)

            balance_sheet = stock.balance_sheet
            cash_flow = stock.cashflow
            income_statement = stock.income_stmt

            document = f"📜 **Financial Statements for {ticker}**\n"

            # Balance Sheet
            document += "\n## 📑 **Balance Sheet (Multi-Year)**\n"
            if not balance_sheet.empty:
                document += balance_sheet.to_string()
            else:
                document += "No balance sheet data available.\n"

            # Cash Flow Statement
            document += "\n## 💵 **Cash Flow Statement (Multi-Year)**\n"
            if not cash_flow.empty:
                document += cash_flow.to_string()
            else:
                document += "No cash flow data available.\n"

            # Income Statement
            document += "\n## 📊 **Income Statement (Multi-Year)**\n"
            if not income_statement.empty:
                document += income_statement.to_string()
            else:
                document += "No income statement data available.\n"

            return document
        except Exception as e:
            return f"Error retrieving financial statements: {str(e)}"

    @tool("market sentiment analysis tool")
    def market_sentiment_tool(ticker):
        """
        Perform market sentiment analysis based on recent stock news for the given ticker.
        Categorizes news as Bullish, Bearish, or Neutral.
        """
        try:
            stock = yf.Ticker(ticker)
            news = stock.news
            sentiment_scores = {"Bullish": 0, "Bearish": 0, "Neutral": 0}

            if not news:
                return "No news available for sentiment analysis."

            document = f"📈 **Market Sentiment Analysis for {ticker}**\n"

            for article in news:
                title = article.get("title", "")
                if any(word in title.lower() for word in ["rises", "growth", "soars", "surge", "gain"]):
                    sentiment_scores["Bullish"] += 1
                elif any(word in title.lower() for word in ["falls", "drop", "decline", "plunge", "loss"]):
                    sentiment_scores["Bearish"] += 1
                else:
                    sentiment_scores["Neutral"] += 1

            total_articles = sum(sentiment_scores.values())
            document += f"\n- **Bullish News:** {sentiment_scores['Bullish']} ({(sentiment_scores['Bullish'] / total_articles) * 100:.2f}%)\n"
            document += f"- **Bearish News:** {sentiment_scores['Bearish']} ({(sentiment_scores['Bearish'] / total_articles) * 100:.2f}%)\n"
            document += f"- **Neutral News:** {sentiment_scores['Neutral']} ({(sentiment_scores['Neutral'] / total_articles) * 100:.2f}%)\n"

            # Conclusion
            if sentiment_scores["Bullish"] > sentiment_scores["Bearish"]:
                document += "\n📊 **Overall Market Sentiment: Positive (Bullish)** 📈"
            elif sentiment_scores["Bearish"] > sentiment_scores["Bullish"]:
                document += "\n📉 **Overall Market Sentiment: Negative (Bearish)** 📉"
            else:
                document += "\n⚖️ **Overall Market Sentiment: Neutral**"

            return document
        except Exception as e:
            return f"Error performing sentiment analysis: {str(e)}"

