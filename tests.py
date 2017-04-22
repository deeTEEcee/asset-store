import unittest
import json
from flask_testing import TestCase
from core.app import db, app

sample_valid_assets = [
    {'name': 'asset_',
     'type': 'satellite',
     'class': 'dove'
    },
    {'name': 'asset__',
     'type': 'satellite',
     'class': 'rapideye'
    },
    {'name': 'asset___',
     'type': 'antenna',
     'class': 'yagi'
    }
]

sample_invalid_assets = [
    {'name': 'asset-bad-type-class',
     'type': 'randomtype',
     'class': 'randomclass'
    },
    {'name': 'asset-bad-satellite-class',
     'type': 'satellite',
     'class': 'badclass'
    },
    {'name': 'asset-bad-antenna-class',
     'type': 'antenna',
     'class': 'isthereasatelliteclass'
    },
    {'name': '_dash-fail',
     'type': 'antenna',
     'class': 'yagi'
    },
    {'name': 'sho',
     'type': 'antenna',
     'class': 'yagi'
    }
]


class BaseTestCase(TestCase):
    def create_app(self):
        return app

    @classmethod
    def setUpClass(cls):
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()


class SimpleTest(BaseTestCase):

    def url(self, path):
        return "/api/v1" + path

    @classmethod
    def setUpClass(cls):
        super(SimpleTest, cls).setUpClass()
        # create custom assets

    def test_initial_assets(self):
        response = self.client.get(self.url("/assets"))
        self.assertEquals(200, response.status_code)

    def test_create_asset(self):
        asset = sample_valid_assets[0]
        response = self.client.post(self.url("/asset/%s" % asset['name']),data=asset)
        self.assertEquals(200, response.status_code)

    def test_create_asset_fail_duplicate(self):
        asset = sample_valid_assets[0]
        response = self.client.post(self.url("/asset/%s" % asset['name']),data=asset)
        self.assertEquals(409, response.status_code)

    def test_create_asset_fail_bad_type(self):
        asset = sample_invalid_assets[0]
        response = self.client.post(self.url("/asset/%s" % asset['name']),data=asset)
        self.assertEquals(422, response.status_code)

    def test_create_asset_fail_bad_satellite_class(self):
        asset = sample_invalid_assets[1]
        response = self.client.post(self.url("/asset/%s" % asset['name']),data=asset)
        self.assertEquals(422, response.status_code)

    def test_create_asset_fail_bad_antenna_class(self):
        asset = sample_invalid_assets[2]
        response = self.client.post(self.url("/asset/%s" % asset['name']),data=asset)
        self.assertEquals(422, response.status_code)

    def test_create_asset_fail_beginning_character_not_allowed(self):
        asset = sample_invalid_assets[3]
        response = self.client.post(self.url("/asset/%s" % asset['name']),data=asset)
        self.assertEquals(422, response.status_code)

    def test_create_asset_fail_name_too_short(self):
        asset = sample_invalid_assets[4]
        response = self.client.post(self.url("/asset/%s" % asset['name']),data=asset)
        self.assertEquals(422, response.status_code)

    def test_get_asset(self):
        asset = sample_valid_assets[0]
        response = self.client.get(self.url("/asset/%s" % asset['name']))
        self.assertEquals(200, response.status_code)

    def test_get_asset_fail(self):
        response = self.client.get(self.url("/asset/nonexistent"))
        self.assertEquals(404, response.status_code)

    def test_get_all_assets(self):
        response = self.client.get(self.url("/assets"))
        data = json.loads(response.data)['data']
        self.assertEquals(1, len(data))
        self.assertEquals(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
