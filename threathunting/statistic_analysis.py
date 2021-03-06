#!/usr/bin/env python
# coding: utf-8
# pylint: disable=unused-wildcard-import

import matplotlib.pyplot as plt
import math
from collections import Counter

class Util:
    @staticmethod
    def entropy(s):
        l = float(len(s))
        return -sum(map(lambda a: (a/l)*math.log2(a/l), Counter(s).values()))

class PrevalenceAnalysis:
    def __init__(self, df):
        self.DF = df
        
    def draw_bar_graph(self):
        ax = self.DF.plot(kind = 'bar', x = 'ClusterId', y = 'ClusterSize', color = 'red', figsize = (20, 10), fontsize = 12, legend = False)
        ax.set_xlabel("Cluster Id", fontsize = 12)
        ax.set_ylabel("Cluster Size", fontsize = 16)
        labels = ax.get_xticklabels()
        for i in range(0, len(labels), 1):
            if i%20 != 0:
                labels[i] = ''
        ax.set_xticklabels(labels)
        plt.show()

