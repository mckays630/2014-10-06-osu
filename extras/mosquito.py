import numpy as np
import matplotlib.pyplot as plt
import sys

def plot_regression(filename):
    year, temperature, rainfall, mosquitos = np.loadtxt(
           filename, skiprows=1, delimiter=',', unpack=True)
    plt.plot(rainfall, mosquitos, 'o')
    coeff = np.polyfit(rainfall, mosquitos, 1)
    fit_to_data = coeff[0] * rainfall + coeff[1]
    plt.plot(rainfall, fit_to_data)
    if filename is sys.stdin:
        plt.savefig('plot.pdf')
    else:
        plt.savefig(filename[:-4] + "-plot.pdf")

for filename in sys.argv:
    if filename[-4:] == '.csv':
        plot_regression(filename)

if len(sys.argv) == 1:
    plot_regression(sys.stdin)
