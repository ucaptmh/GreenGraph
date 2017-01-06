#!/usr/bin/env python

__author__ = 'third'

import requests
from io import BytesIO
from matplotlib import image as img
from greengraph.map import Map
import geopy
import numpy as np
import numpy.testing as npt
import os
import requests
from mock import Mock, patch

lat = 51.5073509
long = -0.1277583


def test_build_map():
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'fixtures', 'london_png.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = Map(lat, long)
        mock_get.assert_called_with(
            'http://maps.googleapis.com/maps/api/staticmap?',
            params=dict(size='400x400', zoom=10, center='51.5073509,-0.1277583',
                        style='feature:all|element:labels|visibility:off', sensor='false', maptype='satellite')
        )


def test_read_map():
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'fixtures', 'london_png.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = Map(lat, long)
        npt.assert_allclose(test_map.pixels, np.load(os.path.join(os.path.dirname(__file__),
                                                                  'fixtures', 'london_numpy.npy')))


def test_green():
    test_green_bool = np.load(os.path.join(os.path.dirname(__file__), 'fixtures', 'london_green_bool.npy'))
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'fixtures', 'london_png.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = Map(lat, long)
        npt.assert_array_equal(Map.green(test_map, threshold=1.1), test_green_bool, "Error in Maps.green")


def test_count_green():
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'fixtures', 'london_png.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = Map(lat, long)
        npt.assert_equal(Map.count_green(test_map, threshold=1.1), 108032, "Error in Map.count_green")


# show_green isn't actually used at present but is an additional feature.
# Needed some updating. Tested as follows:

def test_show_green():
    test_show_green_numpy = np.load(os.path.join(os.path.dirname(__file__), 'fixtures', 'london_show_green.npy'))
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'fixtures', 'london_png.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = Map(lat, long)
        npt.assert_array_equal(img.imread(BytesIO(Map.show_green(test_map, threshold=1.1))), test_show_green_numpy,
                               "Error in Maps.show_green")