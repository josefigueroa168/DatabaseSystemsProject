import matplotlib.pyplot as plt
from numpy.random import rand
import numpy as np

def plot1(data, disease):
    group_data = list(data.values())
    group_names = list(data.keys())
    group_mean = np.mean(group_data)
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.barh(group_names, group_data)
    plt.style.use('fivethirtyeight')
    ax.set(ylabel='States', title='Disease Code: {} by state in 2016'.format(disease))
    ax.axes.get_xaxis().set_visible(False)
    # Add a vertical line, here we set the style in the function call
    ax.axvline(group_mean, ls='--', color='r')
    plt.show()