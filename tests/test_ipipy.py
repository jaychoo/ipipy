#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ipipy
----------------------------------

Tests for `ipipy` module.
"""

import unittest
from flask import json

import requests
from ipipy import ipipy


class TestIpipy(unittest.TestCase):

    def setUp(self):
        self.app = ipipy.setup_web().test_client()

    def is_valid(self, response):
        if 'ip' not in response:
            return False

        if len(response['ip'].split('.')) != 4:
            return False

        return True

    def testCmd(self):
        return self.is_valid(ipipy.main())

    def testWeb(self):
        response = self.app.get('/')
        return self.is_valid(json.loads(response.data))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
