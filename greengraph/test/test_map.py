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


def test_Map():
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'london_png.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = Map(lat, long)
        npt.assert_allclose(test_map.pixels, np.load(os.path.join(os.path.dirname(__file__),
                                                                  'london_numpy.npy')))
        # print("map_test")


def test_green():
    test_green_bool = np.load(os.path.join(os.path.dirname(__file__), 'london_green_bool.npy'))
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'london_png.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = Map(lat, long)
        npt.assert_array_equal(Map.green(test_map, threshold=1.1), test_green_bool, "Error in Maps.green")


def test_count_green():
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'london_png.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = Map(lat, long)
        npt.assert_equal(Map.count_green(test_map, threshold=1.1), 108032, "Error in Map.count_green")


        # class Map(object):
        #
        # def __init__(self, lat, long, satellite=True,
        # zoom=10, size=(400, 400), sensor=False):
        # base = "http://maps.googleapis.com/maps/api/staticmap?"
        #
        # params = dict(
        #     sensor=str(sensor).lower(),
        #     zoom=zoom,
        #                 size="x".join(map(str, size)),
        #                 center=",".join(map(str, (lat, long))),
        #                 style="feature:all|element:labels|visibility:off"
        #             )
        #
        #             if satellite:
        #                 params["maptype"] = "satellite"
        #
        #             self.image = requests.get(base, params=params).content
        #             # Fetch our PNG image data
        #             self.pixels = img.imread(BytesIO(self.image))
        #             # Parse our PNG image as a numpy array
        #
        #     def green(self, threshold):
        #         # Use NumPy to build an element-by-element logical array
        #         greener_than_red = self.pixels[:, :, 1] > threshold * self.pixels[:, :, 0]
        #         greener_than_blue = self.pixels[:, :, 1] > threshold * self.pixels[:, :, 2]
        #         green = np.logical_and(greener_than_red, greener_than_blue)
        #         return green
        #
        #     def count_green(self, threshold=1.1):
        #         return np.sum(self.green(threshold))
        #
        #     def show_green(data, threshold=1.1):
        #         green = self.green(threshold)
        #         out = green[:, :, np.newaxis] * array([0, 1, 0])[np.newaxis, np.newaxis, :]
        #         buffer = BytesIO()
        #         result = img.imsave(buffer, out, format='png')
        #         return buffer.getvalue()