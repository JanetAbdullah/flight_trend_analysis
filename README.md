# Flight Passenger Trend Analysis (1949–1960)

This project performs an in-depth data analysis of the airline passenger data between 1949 and 1960, using the built-in `flights` dataset from the Seaborn library. The analysis is fully custom, not based on any existing public notebooks or articles, and includes detailed breakdowns of temporal trends, volatility, growth behavior, seasonality, and outlier detection.

## Overview
The main objective is to extract meaningful insights from a time series dataset using classic data science techniques—without using machine learning. Key areas of focus include:

- Year-over-year passenger growth and volatility
- Monthly seasonality patterns and variability
- Compound annual growth rate (CAGR)
- Month-to-year contribution analysis
- Z-score-based anomaly detection
- YoY monthly growth rate calculation

## Tools Used
- Python 3.x
- pandas
- matplotlib
- seaborn
- numpy

## How to Run
Make sure the required libraries are installed:
```bash
pip install pandas matplotlib seaborn numpy
```
Then run the analysis:
```bash
python flight_trend_analysis.py
```

## Folder Structure
```
flight_trend_analysis/
├── flight_trend_analysis.py    # Main analysis script
├── README.md                   # Project documentation
```

## Analysis Breakdown
### Yearly Analysis
- Passenger total per year
- Growth rate per year (% change)
- 3-year moving average
- Volatility of growth
- CAGR over 12 years

### Monthly Seasonality
- Average passengers by month
- Standard deviation (volatility) by month

### Heatmap
- Visual representation of passenger distribution across month-year matrix

### Outlier Detection
- Z-score-based detection of unusual monthly values

### Monthly Growth Trends
- Year-over-year monthly growth rates
- Ranking of months by average growth

### Monthly Share
- Each month’s % share of total yearly passengers
- Stacked bar chart comparing seasonal contribution

## Key Insights
- Identifies which years had the strongest and weakest growth
- Detects outlier months that significantly differ from normal patterns
- Shows which months consistently dominate travel volume
- Calculates monthly contribution share across years
- Measures average monthly volatility and relative performance

## License
This project is open-source and intended for educational and portfolio purposes. All code is original and created manually for demonstration of data science skills without using machine learning.

---

**Author:** Janet Abdullah  
**GitHub:** [https://github.com/JanetAbdullah]  
Feel free to fork and adapt this analysis to your own use!

