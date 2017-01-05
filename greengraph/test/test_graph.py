#!/usr/bin/env python
__author__ = 'third'
import numpy as np
import geopy
from greengraph.map import Map
from greengraph.graph import Greengraph
import os
from io import BytesIO
import numpy as np
import numpy.testing as npt
import yaml
from mock import Mock, patch
from nose.tools import assert_equal


def test_build_graph():
    with open(os.path.join(os.path.dirname(__file__),
                           'fixtures', 'build.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            answer = Greengraph(**fixture)
            assert_equal(answer.start, fixture['start'])
            assert_equal(answer.end, fixture['end'])
            assert_equal(answer.geocoder.domain, "maps.google.co.uk")


def test_geolocate():
    with patch.object(geopy.geocoders.GoogleV3, 'geocode') as mock_geocode:
        with open(os.path.join(os.path.dirname(__file__),
                               'fixtures', 'build.yaml')) as fixtures_file:
            fixtures = yaml.load(fixtures_file)
            for fixture in fixtures:
                answer = Greengraph(**fixture)
                answer.geolocate(fixture['start'])
                mock_geocode.assert_called_with(fixture['start'], exactly_one=False)
                answer.geolocate(fixture['end'])
                mock_geocode.assert_called_with(fixture['end'], exactly_one=False)


def test_location_sequence():
    test_sequence_numpy = np.load(os.path.join(os.path.dirname(__file__), 'ox_london_seq.npy'))
    with patch.object(geopy.geocoders.GoogleV3, 'geocode') as mock_geocode:
        answer = Greengraph('Oxford', 'London')
        mock_seq = answer.location_sequence((51.7520209, -1.2577263), (51.5073509, -0.1277583), 5)
        npt.assert_array_almost_equal(mock_seq, test_sequence_numpy, decimal=2)


def test_green_between():
    mock_image_start = open(os.path.join(os.path.dirname(__file__),
                                         'london_png.png'), 'rb')
    mock_image_end = open(os.path.join(os.path.dirname(__file__),
                                       'london_png.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image_start.read())) as mock_get:
        answer = Greengraph('Oxford', 'London')
        mock_green = answer.green_between(2)
        npt.assert_array_almost_equal(mock_green, [108032, 108032], decimal=2)






        # class Greengraph(object):
        # def __init__(self, start, end):
        # self.start = start
        # self.end = end
        # self.geocoder = geopy.geocoders.GoogleV3(
        # domain="maps.google.co.uk")
        #
        # def geolocate(self, place):
        # return self.geocoder.geocode(place,
        # exactly_one=False)[0][1]
        #
        # def location_sequence(self, start, end, steps):
        # lats = np.linspace(start[0], end[0], steps)
        # longs = np.linspace(start[1], end[1], steps)
        # return np.vstack([lats, longs]).transpose()
        #
        # def green_between(self, steps):
        # return [Map(*location).count_green()
        # for location in self.location_sequence(
        # self.geolocate(self.start),
        # self.geolocate(self.end),
        # steps)]