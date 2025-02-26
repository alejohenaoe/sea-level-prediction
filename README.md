# Sea Level Predictor

# Sea Level Prediction

This project analyzes historical sea level data and uses linear regression to predict future sea levels. The goal is to provide a clear visualization of how sea levels have changed since 1880 and to forecast trends up to the year 2050.

## Project Overview

The project leverages historical data from the EPA provided in the `epa-sea-level.csv` file. It processes the data, fits a linear regression model, and generates a visualization that displays both historical measurements and future predictions.

### Data Analysis Tools & Techniques

- **Python**: The primary programming language used for data processing and analysis.
- **Pandas**: Utilized for data manipulation and cleaning of the CSV dataset.
- **NumPy**: Supports efficient numerical computations on large arrays and matrices.
- **Matplotlib**: Employed to create visualizations, including the plot of historical data and predictions.
- **Scikit-learn**: Implements linear regression to model the trend in sea level data and make future predictions.

The script in `sea_level_predictor.py` performs the following tasks:
- Reads and cleans the historical sea level data.
- Fits a linear regression model on the dataset.
- Generates a plot that shows:
  - The scatter plot of historical sea level data.
  - The regression line representing the trend.
  - The projected sea level rise up to 2050.

## Running the Project

To run the project and generate the sea level prediction plot:



This is the boilerplate for the Sea Level Predictor project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor
