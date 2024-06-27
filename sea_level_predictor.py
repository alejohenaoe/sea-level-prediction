import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(16, 8))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='gray')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = np.arange(1880, 2051)
    line_of_best_fit = intercept + slope * years_extended

    plt.plot(years_extended, line_of_best_fit, color='red', linestyle='dashed', label=f'Line of best fit\nFrom: 1880 - 2050')
    plt.title('Sea Level Rise')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (cm)')
    plt.legend()

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    df_2000.head(20)

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    years_extended_2 = np.arange(2000, 2051)
    line_of_best_fit_2 = intercept2 + slope2 * years_extended_2
        
    plt.plot(years_extended_2, line_of_best_fit_2, color='teal', linestyle='dashed', label='Line of best fit\nFrom: 2000 - 2050')
    plt.axvline(2000, linestyle='dotted')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()