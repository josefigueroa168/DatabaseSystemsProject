import matplotlib.pyplot as plt
import matplotlib
from numpy.random import rand
import numpy as np

def plot1(data, question):
    group_data = list(data.values())
    group_names = list(data.keys())
    group_mean = np.mean(group_data)
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.barh(group_names, group_data)
    plt.style.use('fivethirtyeight')
    ax.set(ylabel='States', title='Percent {}'.format(question))
    # Add a vertical line, here we set the style in the function call
    ax.axvline(group_mean, ls='--', color='r')
    plt.show()

def binaryPieChart(key, val):
    fig, ax = plt.subplots(figsize=(12, 10))
    val = val / 100
    neg = 1 - val
    vals = [val, neg]
    labels = ['Yes', 'No']
    plt.pie(vals, labels=labels)
    plt.title(key)
    plt.show()