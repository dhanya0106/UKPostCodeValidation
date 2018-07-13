import os
import json
from unittest import TestCase
from UKPostCode.UKPostCode import UKPostCode

'''
Postcodes.txt contains all the post codes from UK. This file is downloaded from
the UK government website.

This script runs checks out validation script against all the UK post codes.
'''
class TestPostalCode(TestCase):
    def setUp(self):
        filepath = os.getcwd()
        filename = os.path.join(filepath,'postcodes.txt')
        with open(filename, 'r') as handle:
            post_codes_str = handle.read()
        self.all_post_codes = json.loads(post_codes_str)


    def test_validate_all(self):
        for key in self.all_post_codes.keys():
            values = self.all_post_codes[key].split(',')
            for val in values:
                obj = UKPostCode()
                value = key + val
                self.assertTrue(obj.validate_postcode(value), value)
