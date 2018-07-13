A program to validate format UK Post Code:

Usage:

Validation:
-----------

>>> from UKPostCode import UKPostCode
>>> obj = UKPostCode()
>>> obj.validate_postcode('EC1M3AF')
True
>>> obj.validate_postcode('EC1MA')
False

Returns True or False boolean values.

Formatting:
-----------
>>> from UKPostCode import UKPostCode
>>> obj = UKPostCode()
>>> obj.format_postcode('EC1m3a  f')
'EC1M 3AF'


Format function will internally validate post codes and raises ValueError if
postcode supplied is not valid.
Returns the formatted Post code values of type string.
