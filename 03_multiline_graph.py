#!/usr/bin/env python3

# Python 3.9.5

# 03_multiline_graph.py

# Purpose: Drawing a multiline graph

# Dependencies
import matplotlib.pyplot as plt
import numpy as np

# Producing data with the functions sin(x), cos(x):
x = np.arange(0, 15, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# Setting parameters for mutiline graph visualization:
labels = ['sin(x)', 'cos(x)']
plt.plot(x, y1, x, y2)
plt.legend(labels, loc='lower right')
plt.grid()
plt.show()
