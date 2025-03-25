import streamlit as st
from crewai import Agent
from langchain_groq import ChatGroq
from fin_tools import SearchTool
import re

class FinAgents:
    def llm(self):
        return ChatGroq(
            model="mixtral-8x7b-32768", 
            temperature=0, 
            api_key=st.secrets['GROQ_API']
        )

    def fin_agent(self):
        return Agent(
            role="Financial Analyst",
            goal="Uncover main financial situation and insights about company {ticker}",
            backstory="You work at an asset management firm as an analyst, highly skilled in analyzing stock {ticker} data based on financial reports.",
            verbose=True,
            memory=True,
            max_iter=5,
            allow_delegation=False,
            tools=[SearchTool.fin_data_tool],
            llm=self.llm(),
        )

    def news_agent(self):
        return Agent(
            role="News Analyst",
            goal="Analyze news and market sentiments for company {ticker}",
            backstory="You work in a news office at an asset management firm. Your goal is to track and categorize news for {ticker}, identifying key trends.",
            verbose=True,
            memory=True,
            max_iter=5,
            allow_delegation=False,
            tools=[SearchTool.search_web_tool],
            llm=self.llm(),
        )

    def reporter_agent(self):
        return Agent(
            role="Financial Reporter",
            goal="Create compelling financial reports for stock {ticker}",
            backstory="You are a renowned financial content strategist, skilled at transforming complex financial data into engaging and insightful reports for {ticker}.",
            verbose=True,
            memory=True,
            max_iter=5,
            allow_delegation=False,
            llm=self.llm(),
        )

class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']
        self.color_index = 0

    def write(self, data):
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)
        task_match = re.search(r'task\s*:\s*"?([^"\n]+)"?', cleaned_data, re.IGNORECASE)
        if task_match:
            st.toast(f":robot_face: {task_match.group(1).strip()}")

        highlight_phrases = {
            "Entering new CrewAgentExecutor chain": "CrewAgentExecutor Started",
            "City Selection Expert": "City Selection Active",
            "Local Expert at this city": "Local Expert Engaged",
            "Amazing Travel Concierge": "Travel Concierge in Action",
            "Finished chain.": "Execution Complete"
        }

        for phrase, label in highlight_phrases.items():
            if phrase in cleaned_data:
                self.color_index = (self.color_index + 1) % len(self.colors)
                cleaned_data = cleaned_data.replace(phrase, f":{self.colors[self.color_index]}[{label}]")

        self.buffer.append(cleaned_data)

        if "\n" in data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []
