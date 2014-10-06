"""Creates dotplot with linear regression of rainfall vs. mosquitos.

Input: comma-separated values of year, temperature, rainfall, and number
of mosquitos via filename(s) or standard input

Output: pdf of the plot; if data is from standard input: output in plot.pdf
if data is from a file: filename-plot.pdf"""

import numpy as np
import matplotlib.pyplot as plt
import sys

def plot_regression(filename):
    """Plots data and linear regression of rainfall vs. mosquitos"""
    year, temperature, rainfall, mosquitos = np.loadtxt(
           filename, skiprows=1, delimiter=',', unpack=True)
    plt.plot(rainfall, mosquitos, 'o') # 'o' will plot dots instead of lines
    # calculate values for linear regression (polynomial fit of degree = 1):
    coeff = np.polyfit(rainfall, mosquitos, 1)
    # calculate y-values with the formula: y = m * x + b
    fit_to_data = coeff[0] * rainfall + coeff[1]
    # plot the resulting linear regression line
    plt.plot(rainfall, fit_to_data)

    # decide whether the plot is written to 'plot.pdf' or 'filename-plot.pdf'
    if filename is sys.stdin:
        plt.savefig('plot.pdf')
    else:
        plt.savefig(filename[:-4] + "-plot.pdf")

for filename in sys.argv:
    # only plot_regression for command line arguments that end in ".csv"
    # skips the first sys.argv value that is "mosquito.py"
    if filename[-4:] == '.csv':
        plot_regression(filename)

# if no filenames were given, sys.argv only contains "mosquito.py"
# therefore, expect input from sys.stdin (standard input)
# this is what allows us to pipe data into the program, for example:
# cat A1_mosquito_data.csv | python mosquito.py
if len(sys.argv) == 1:
    plot_regression(sys.stdin)
