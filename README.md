# GreenGraph
This programme produces a plot of a graph that creates a rudimentary measure of the amount of green land between two cities. This is acheived by taking satellite images between the two locations over a given number of steps.

##Installation
To install run the following code:
* From command: `python setup.py install`
* Using pip: `pip install git+git://github.com/ucaptmh/GreenGraph`
* Un-installation achieved by either a) deleting the relevant files or b) running `pip uninstall greengraph`

##Usage
Software may be ran from command line by the following:

`greengraph [-h] --start START --end END --steps STEPS --out OUT`
* `START` : The starting location
* `END` : The final location
* `STEPS` : The number of steps to use between the two locations
* `OUT` : The output file for the graph

Example: `greengraph --start Sydney --end Melbourne --steps 20 --out GreenAus.png`

This would produce a graph named GreenAus.png showing the number of green pixels in 20 satellite images taken in equal steps between Sydney and Melbourne
