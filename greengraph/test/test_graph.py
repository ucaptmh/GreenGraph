#!/usr/bin/env python
__author__ = 'third'
import numpy as np
import geopy
from greengraph.map import Map
from greengraph.graph import Greengraph
import os
import numpy as np
import numpy.testing as npt
import yaml
from nose.tools import assert_equal


def test_build_graph():
    with open(os.path.join(os.path.dirname(__file__),
                           'fixtures', 'build.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            answer = Greengraph(**fixture)
            assert_equal(answer.start, fixture['start'])
            assert_equal(answer.end, fixture['end'])


# class Greengraph(object):
# def __init__(self, start, end):
# self.start = start
#         self.end = end
#         self.geocoder = geopy.geocoders.GoogleV3(
#             domain="maps.google.co.uk")
#
#     def geolocate(self, place):
#         return self.geocoder.geocode(place,
#                                      exactly_one=False)[0][1]
#
#     def location_sequence(self, start, end, steps):
#         lats = np.linspace(start[0], end[0], steps)
#         longs = np.linspace(start[1], end[1], steps)
#         return np.vstack([lats, longs]).transpose()
#
#     def green_between(self, steps):
#         return [Map(*location).count_green()
#                 for location in self.location_sequence(
#                 self.geolocate(self.start),
#                 self.geolocate(self.end),
#                 steps)]