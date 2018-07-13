A program to validate format UK Post Code:

Installation instructions:
===========================

Supported on Python3 only:

>>> git clone https://github.com/dhanya1/UKPostCodeValidation.git
>>> cd UKPostCodeValidation
>>> pip install .

( I was unable to publish to PyPI at the moment due to name clash. I did not make that change to the code yet, so as to not break the code. )

Usage:

Validation:
-----------

>>> from UKPostCode.UKPostCode import UKPostCode
>>> obj = UKPostCode()
>>> obj.validate_postcode('EC1M3AF')
True
>>> obj.validate_postcode('EC1MA')
False

Returns True or False boolean values.

Formatting:
-----------
>>> from UKPostCode.UKPostCode import UKPostCode
>>> obj = UKPostCode()
>>> obj.format_postcode('EC1m3a  f')
'EC1M 3AF'


Format function will internally validate post codes and raises ValueError if postcode supplied is not valid.
Returns the formatted Post code values of type string.
