import unittest
from UKPostCode.UKPostCode import UKPostCode


class TestPostalCode(unittest.TestCase):
    def setUp(self):
        self.positive_values = [
            'EC1A 1BB',  # special cases
            'BS98 1TL',
            'CF10 1BH',
            'CV4 8UW',
            'DA1 1RT',
            'SW1W 0NY',  # normal
            'M1 1AE',
            'B33 8TH',
            'CR2 6XH',
            'DN55 1PT',
            'PO16 7GZ',
            'GU16 7HF'
        ]

        self.negative_values = [
            'QN55 1PT',  # Bad letter in 1st position
            'QN55 1PT',  # Bad letter in 1st position
            'DI55 1PT',  # Bad letter in 2nd position
            'W1Z 0AX',  # Bad letter in 3rd position
            'EC1Z 1BB',  # Bad letter in 4th position
            'AA34 1ZO'   # Bad letter in 2nd grouo
            'DN55 1CT',  # Bad letter in 2nd group
            'A11A 1AA',  # Invalid digits in 1st group
            'AA11A 1AA',  # 1st group too long
            'AA11 1AAA',  # 2nd group too long
            'AA11 1AAA',  # 2nd group too long
            'AAA 1AA',  # No digit in 1st group
            'AA 1AA',  # No digit in 1st group
            'A 1AA',  # No digit in 1st group
            '1A 1AA',  # Missing letter in 1st group
            '1 1AA',  # Missing letter in 1st group
            '11 1AA',  # Missing letter in 1st group
            'AA1 1A',  # Missing letter in 2nd group
            'AA1 1',  # Missing letter in 2nd group

        ]

        self.positive_badformat = [
            '   EC1A 1BB',  # whitespace before
            'BS98 1TL   ',  # whitespace after
            'Cf101bH',      # Mixed case
            'CV4 8UW'       # Normal case
        ]

    def test_validate_postcode(self):
        for value in self.positive_values:
            obj = UKPostCode()
            self.assertTrue(obj.validate_postcode(value), value)
        for value in self.negative_values:
            obj = UKPostCode()
            self.assertFalse(obj.validate_postcode(value), value)

    def test_format_postcode(self):
        for i, value in enumerate(self.positive_badformat):
            obj = UKPostCode()
            self.assertEqual(obj.format_postcode(value),
                             self.positive_values[i], value)


if __name__ == '__main__':
    unittest.main()