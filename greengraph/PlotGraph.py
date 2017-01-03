__author__ = 'third'
from matplotlib import pyplot as plt
from graph import Greengraph

def PlotGraph(start='New York', end='Chicago', steps=20,out='graph.png'):
    mygraph = Greengraph(start,end)
    data = mygraph.green_between(steps)
    plt.plot(data)
    #plt.savefig(out)
    plt.show()