#!/usr/bin/env python
__author__ = 'third'
from matplotlib import pyplot as plt
from greengraph.graph import Greengraph


def plotGraph(start='Sydney', end='Melbourne', steps=20, out: object="graph.png"):
    mygraph = Greengraph(start, end)
    data = mygraph.green_between(steps)
    plt.plot(data)
    #plt.show()
    #plt.savefig(out)

    if out:
        plt.savefig(out)

    plt.show()