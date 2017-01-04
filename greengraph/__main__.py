__author__ = 'third'
from argparse import ArgumentParser

from greengraph.PlotGraph import plotGraph


def process():
    parser = ArgumentParser(
        description="Produce a graph of number of green pixels in satellite images between two locations")
    parser.add_argument("--start", required=True,
                        help='Starting location')
    parser.add_argument("--end", required=True,
                        help='Final location')
    parser.add_argument("--steps", required=True,
                        help='Number of steps desired between starting and ending locations')
    parser.add_argument("--out",  required=True,
                        help="Filename of output")

    arguments = parser.parse_args()

    plotGraph(arguments.start, arguments.end, arguments.steps, arguments.out)

if __name__ == "__main__":
    process()