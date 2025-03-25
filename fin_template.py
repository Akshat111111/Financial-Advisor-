fin_template = """

# RIL (Reliance Industries Limited) Financial Report

## Company Information

| Name | Ticker | Stock Price | Market Cap |
|---|---|---|---|
| {symbol} | 'RIL' | {currentPrice} ₹ | {marketCap} Cr ₹ |

---

## 🏛️ Basic Company Information :
[Summary in 4 bullets of {longBusinessSummary}]

### Company :
"Reliance Industries Limited operates as a diversified conglomerate in India and internationally. The company engages in hydrocarbon exploration, production, refining, and petrochemicals. It has a strong presence in retail, digital services, telecommunications (Jio), and green energy. The company also focuses on new-age businesses, including AI-driven digital transformation and sustainability projects. Reliance is known for its strategic partnerships with global firms like Facebook, Google, and Microsoft, positioning it as a leader in India's digital revolution."

## 🌐 Main Company Information :

| Company Information | - |
|---|---|
| Symbol | RIL |
| Short Name | Reliance Industries Ltd |
| Current Price | {currentPrice} ₹ |
| Market Cap | {marketCap} Cr ₹ |
| Country | India |
| Industry & Sector | 'Conglomerate' / 'Energy, Retail, Telecom' |
| CEO | 'Mr. Mukesh Ambani' |
| Website | 'https://www.ril.com' |
| Full-Time Employees | {fullTimeEmployees} |
| Exchange | NSE / BSE |

### Analysis :
Your analysis here

## 📊 Financial Ratios 
* Analysis of the financial ratios in 5 bullets

| Financial Ratios | - |
|---|---|
| P/E Ratio | {trailingPE} |
| Forward P/E | {forwardPE} |
| Price to Sales (TTM) | {priceToSalesTrailing12Months} |
| PEG Ratio | {pegRatio} |
| Enterprise to Revenue | {enterpriseToRevenue} |
| Enterprise to EBITDA | {enterpriseToEbitda} |
| Return on Assets (ROA) | {returnOnAssets} |
| Return on Equity (ROE) | {returnOnEquity} |
| Price to Book | {priceToBook} |

## 📊 Company Valuation - Financial Ratios 
* Analysis of the company valuation in 10 bullets and recommendations

| Financial Metrics | - |
|---|---|
| Total Revenue | {totalRevenue} Cr ₹ |
| Revenue Per Share | {revenuePerShare} ₹ |
| Enterprise Value | {enterpriseValue} Cr ₹ |
| Total Cash | {totalCash} Cr ₹ |
| Profit Margins | {profitMargins} % |
| Book Value | {bookValue} ₹ |
| Revenue Growth | {revenueGrowth} % |
| Earnings Growth | {earningsGrowth} % |
| Quarterly Earnings Growth | {earningsQuarterlyGrowth} % |
| Gross Margins | {grossMargins} % |
| EBITDA Margins | {ebitdaMargins} % |
| Operating Margins | {operatingMargins} % |
| Net Income | {netIncomeToCommon} Cr ₹ |
| Trailing EPS | {trailingEps} ₹ |
| Forward EPS | {forwardEps} ₹ |
| Total Cash Per Share | {totalCashPerShare} ₹ |
| EBITDA | {ebitda} Cr ₹ |
| Free Cash Flow | {freeCashflow} Cr ₹ |
| Operating Cash Flow | {operatingCashflow} Cr ₹ |

## 📉 Revenue Growth :
Quarter | Revenue (in Crores) | Growth Rate  
- Q1 2024 | {revenueQ1} | {growthQ1} %  
- Q2 2024 | {revenueQ2} | {growthQ2} %  
- Q3 2024 | {revenueQ3} | {growthQ3} %  
❗ RIL’s revenue has been steadily increasing, with a growth rate of {growthQ3} % in Q3 2024.

## 📉 Price Action :
Your analysis here

| Price Action | - |
|---|---|
| Previous Close | {previousClose} ₹ |
| Open | {open} ₹ |
| Day Low | {dayLow} ₹ |
| Day High | {dayHigh} ₹ |
| Beta | {beta} |
| Volume | {volume} |
| Average Volume | {averageVolume} |

## 💵 Dividends :
Your analysis here

| Dividends | - |
|---|---|
| Dividend Rate | {dividendRate} ₹ |
| Dividend Yield | {dividendYield} % |
| Ex-Dividend Date | {exDividendDate} |
| Payout Ratio | {payoutRatio} % |
| Five-Year Avg Dividend Yield | {fiveYearAvgDividendYield} % |

## 💸 Debt Situation :
Your analysis here

| Debt Situation  | - |
|---|---|
| Total Debt | {totalDebt} Cr ₹ |
| Quick Ratio | {quickRatio} |
| Current Ratio | {currentRatio} |
| Debt to Equity | {debtToEquity} |

## 🕵️ Recommendations :
Your analysis here

| Recommendations | - |
|---|---|
| Target High Price | {targetHighPrice} ₹ |
| Target Low Price | {targetLowPrice} ₹ |
| Target Mean Price | {targetMeanPrice} ₹ |
| Target Median Price | {targetMedianPrice} ₹ |
| Recommendation Mean | {recommendationMean} |
| Recommendation Key | {recommendationKey} |
| Number of Analyst Opinions | {numberOfAnalystOpinions} |

## 🎢 Risk Board :
Your analysis and conclusion here

| Risk Board | - |
|---|---|
| Audit Risk | {auditRisk} |
| Board Risk | {boardRisk} |
| Compensation Risk | {compensationRisk} |
| Shareholder Rights Risk | {shareHolderRightsRisk} |
| Overall Risk | {overallRisk} |

## ⚡ Short Interest :
Your analysis and recommendations here

| Short Situation | - |
|---|---|
| Float Shares | {floatShares} |
| Shares Outstanding | {sharesOutstanding} |
| Shares Short | {sharesShort} |
| Shares Short (Prior Month) | {sharesShortPriorMonth} |
| Short Ratio | {shortRatio} |
| Short Percent of Float | {shortPercentOfFloat} |
| Held Percent Insiders | {heldPercentInsiders} |
| Held Percent Institutions | {heldPercentInstitutions} |

---
## Conclusion and Recommendations :
Your final conclusion and recommendations here, in 3 paragraphs.

---
## Industry Benchmarking & Final Takeaway:
- Compare RIL’s financials with **competitors like Tata, Adani, and ONGC**.
- Highlight key differentiators in **growth, profitability, and risk factors**.
- Provide a clear **investment recommendation** based on valuation.

"""  

