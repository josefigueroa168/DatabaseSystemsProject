import matplotlib.pyplot as plt
import matplotlib
from numpy.random import rand
import numpy as np
import pandas as pd

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
    
def plot2(data):
    group_data = list(data.values())
    group_names = list(data.keys())
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.barh(group_names, group_data)
    plt.style.use('fivethirtyeight')
    ax.set(ylabel='Percent yes')
    # Add a vertical line, here we set the style in the function call
    plt.show()
    
def plot3(data):
    q_x = data.loc[0,:][1]
    q_y = data.loc[1,:][1]
    state_name = []
    state_x = []
    state_y = []
    for i in range(0, data.shape[0], 2):
        state_name.append(data.loc[i,:][0])
        state_x.append(data.loc[i,:][2])
        state_y.append(data.loc[i+1,:][2])
    fig, ax = plt.subplots()
    ax.scatter(state_x, state_y)
    for i in range(len(state_name)):
        ax.annotate(state_name[i], (state_x[i], state_y[i]))
    ax.set_xlabel(q_x)
    ax.set_ylabel(q_y)
    plt.show()