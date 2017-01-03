__author__ = 'third'
from matplotlib import pyplot as plt
from greengraph.graph import Greengraph


def plotGraph(start='New York', end='Chicago', steps=20, out='graph.png'):
    mygraph = Greengraph(start, end)
    data = mygraph.green_between(steps)
    plt.plot(data)

    if out:
        plt.savefig(out)
    plt.show()