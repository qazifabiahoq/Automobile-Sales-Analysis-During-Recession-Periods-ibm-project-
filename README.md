#  Automobile Sales Analysis During Recession Periods

Introduction: The automobile industry, being highly sensitive to economic fluctuations, often experiences significant changes in sales during periods of recession. The recession periods, marked by high unemployment rates, low consumer confidence, and reduced GDP growth, lead to altered consumer behavior, affecting automobile purchases. This project aims to analyze historical automobile sales data during various recession periods to understand how key economic factors, such as GDP, unemployment rate, consumer confidence, seasonality, and vehicle types, influence automobile sales trends. By examining both recession and non-recession periods, this analysis identifies the resilience of specific vehicle types and sheds light on the factors contributing to sales changes.

The project is divided into two parts: data visualization (Tasks 1.1 - 1.10) and the development of an interactive dashboard using Dash. Through a detailed exploration of the data, including trends in sales by vehicle type, economic indicators, and advertising expenditure, this study provides valuable insights into the impact of recessions on automobile sales.

Part 1: Data Visualization (Tasks 1.1 - 1.10)

Task 1.1: Line Chart of Automobile Sales Fluctuations from Year to Year
Question: How do automobile sales fluctuate from year to year?
Findings:

Sales peaked in 1995, showcasing a period of economic stability and consumer confidence.
A sharp decline in sales is observed during the 2007-2009 recession period, with sales dropping to around 700 units.
A similar decline in sales occurred during the 1981-1982 recession period, indicating a direct correlation between recessions and sales.
Task 1.2: Sales Trend per Vehicle Type During Recession Periods
Question: Is there a noticeable difference in sales trends between different vehicle types during recession periods?
Findings:

Sports cars and supermini cars show resilience or growth during recessions, indicating a stable niche market that remains less impacted by economic downturns.
Medium family cars and small family cars exhibit more sensitivity to economic changes, with sales fluctuating significantly during recessions.
The consistent upward trend in sports vehicle sales highlights the stability of the luxury market even during recessions.
Task 1.3: Comparison of Sales Trends per Vehicle Type During Recession and Non-Recession Periods
Question: How do automobile sales of different vehicle types compare during recession and non-recession periods?
Findings:

Sales during non-recession periods average 2,600 units, while during recession periods, sales drop to around 600-700 units, showing the profound impact of economic downturns on sales.
Executive cars and sports cars are the most affected by recessions, reflecting that higher-end vehicles face greater reductions in sales due to consumer spending cuts.
Medium family cars show a more significant decline in sales during recessions, while small family cars remain relatively stable, indicating their status as an essential commodity for consumers.
Task 1.4: GDP Comparison During Recession and Non-Recession Periods
Question: How did GDP vary over time during recession and non-recession periods?
Findings:

GDP consistently remains lower during recession periods, reflecting the overall economic contraction that typically accompanies recessions.
This decline in GDP is expected to affect automobile sales, as lower GDP levels generally lead to reduced consumer spending, thus affecting the demand for cars.
Task 1.5: Bubble Plot for Seasonality Impact on Automobile Sales
Question: How has seasonality impacted automobile sales during non-recession years?
Findings:

Seasonality plays a significant role in automobile sales, particularly in the month of April, which stands out for its high sales volumes.
The size of the bubble in April indicates that seasonality has a substantial impact on sales during this period, with consumers more likely to make automobile purchases during specific times of the year.
Task 1.6: Scatter Plot for Correlation Between Vehicle Price and Sales During Recessions
Question: What is the correlation between the average vehicle price and automobile sales during recessions?
Findings:

There is no clear correlation between the average vehicle price and automobile sales during recession periods. This suggests that other factors, such as consumer preferences and external economic influences (like consumer confidence), may have a more significant role in determining sales trends.
Task 1.7: Pie Chart for Advertising Expenditure During Recession and Non-Recession Periods
Question: How did advertising expenditure change during recession and non-recession periods?
Findings:

XYZAutomotives spent a significantly larger portion of its advertising budget during non-recession periods (79%) compared to recession periods (21%).
This trend highlights that the company allocates a more substantial budget for advertising during favorable economic conditions, likely to maximize the impact of their marketing efforts.
Task 1.8: Pie Chart for Advertising Expenditure per Vehicle Type During Recession Period
Question: What is the share of each vehicle type in total advertising expenditure during recessions?
Findings:

During recessions, sports cars and executive cars garnered a more substantial share of the advertising expenditure.
The focus on these vehicle types during recessions may reflect the company’s attempt to maintain a stable customer base within the luxury and niche vehicle markets.
Task 1.9: Line Plot to Analyze the Effect of Unemployment Rate on Vehicle Type and Sales During the Recession Period
Question: How does the unemployment rate affect vehicle type and sales during recession periods?
Findings:

Higher unemployment rates are correlated with decreased sales in most vehicle categories, especially in the medium family car segment, indicating that higher unemployment leads to reduced consumer purchasing power.
The sports car segment appears to be less affected, possibly due to the more affluent customer base for these vehicles.
Task 1.10: Recession Impact on Automobile Sales by City (Choropleth Map)
Question: How does the recession impact automobile sales across different cities?
Findings:

Recession Impact: The dataset focuses on automobile sales during recession periods (Recession = 1). It shows how factors like consumer confidence and unemployment rates affect sales across cities.
City-wise Sales:
California had the highest sales at 18,982.6 units, indicating resilience during the recession.
New York also showed strong sales (19,954.6 units), while Georgia and Illinois had slightly lower figures (17,470.5 and 16,874.7 units, respectively).
Economic Factors: Fluctuations in consumer confidence and unemployment rates impacted sales. Higher consumer confidence generally corresponded with better sales during recession periods.
Geographical Trends: Larger markets like California and New York showed stronger sales during the recession, suggesting higher resilience in these regions compared to smaller or less economically diverse cities.
Part 2: Dash App Development

Objective:
The second part of the project involved developing an interactive dashboard using Dash to allow users to explore the recession period's impact on automobile sales dynamically.

Features Implemented:

Line Charts: Displayed trends in automobile sales over time, including recession periods.
Pie Charts: Represented the distribution of advertising expenditure during recessions and non-recession periods.
Bar Plots: Compared vehicle sales by type during recession vs. non-recession periods.
Interactive Filters: Allowed users to filter the data by vehicle type, recession periods, and other key factors like GDP and unemployment rate.
Insights from the Dash App:

Users can interactively analyze how different recession periods impacted automobile sales, advertising expenditure, and other factors.
The dashboard provides an engaging way to explore the trends in sales fluctuations, helping companies understand market dynamics during economic downturns.
Further Development:

Building upon the analysis, further exploration could include the following:

Extended Timeframes: Analyzing longer periods beyond the recession years to understand recovery trends.
Economic Forecasting Models: Developing predictive models to forecast the effects of future recessions on automobile sales based on current economic indicators.
Consumer Sentiment Analysis: Integrating consumer sentiment data to provide a deeper understanding of consumer behavior during economic downturns.
Conclusion:

This project offers valuable insights into how automobile sales are affected by various economic factors, especially during recession periods. Through a combination of data visualization techniques and an interactive Dash app, we can gain a deeper understanding of trends in automobile sales, which helps automobile companies make informed decisions to mitigate the negative impacts of recessions on sales. The analysis reveals that while most vehicle types are significantly affected by economic downturns, some niche markets, such as sports cars, exhibit resilience. Moreover, advertising strategies and consumer confidence during recessions also play a crucial role in sales performance.

Acknowledgement:

This project was completed as part of the IBM Data Science Professional Certificate program. Special thanks to Dr. Pooja for providing valuable guidance, and Alison Woolford for their contributions. The work presented here was authored and contributed by me,
