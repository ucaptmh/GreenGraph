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
from itertools import cycle
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
    mock_image_end = open(os.path.join(os.path.dirname(__file__),
                                       'london_png.png'), 'rb')
    data = cycle([(51.7520209, -1.2577263), (51.5073509, -0.1277583)])
    dummy_geolocate = Mock(name="geolocate", side_effect=data)
    dummy_green=Mock(name="count_green", side_effect=[158198, 108032])
    with patch('requests.get', return_value=Mock(content=mock_image_end.read())) as mock_get:
        with patch.object(Greengraph, 'geolocate', dummy_geolocate) as mock_geolocate:
            with patch.object(Map,'count_green', dummy_green) as mock_count_green:
                answer1 = Greengraph('Oxford', 'London')
                mock_green = answer1.green_between(2)
                npt.assert_array_equal(mock_green, [158198, 108032])

