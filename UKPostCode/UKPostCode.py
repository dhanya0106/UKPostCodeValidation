import re

PATTERN = '^([A-PR-UWYZ][A-HK-Y]?)' \
          '([\d]{1})' \
          '([\dA-Z]?)' \
          '([\d]{1}[ABD-HJLNPQ-Z]{2})$'


class UKPostCode(object):
    def __init__(self):
        self.post_code = {}

    def __extract(self, s):
        s = s.strip()
        # Capture Area code, District code and Inward code respectively
        codes = re.match(PATTERN, s)
        if codes is None:
            return False
        parts = list(codes.groups())
        optional_char = parts.pop(2)
        self.post_code['area_code'] = parts[0]
        self.post_code['district_code'] = parts[1]
        self.post_code['inward_code'] = parts[2]
        res = self.__validate(parts, optional_char)
        return res
        
    def __validate(self, parts, optional_char):
        if None in parts:
            return False
        else:
            if optional_char is not None:
                if optional_char.isalpha():
                    if len(self.post_code['area_code']) == 1\
                    and optional_char not in 'ABCDEFGHJKPSTUW':
                            return False
                    elif len(self.post_code['area_code']) == 2\
                    and optional_char not in 'ABEHMNPRVWXY':
                            return False
                    else:
                        return False
                self.post_code['district_code'] = \
                    self.post_code['district_code'] + optional_char
            return True

    def __validate_special_case(self, s):
        codes = re.match(r'^([Gg][Ii][Rr] 0[Aa]{2})$',s)
        if codes:
            self.__parts = ('G','I','0AA')
            self.post_code = {'area_code': 'G',
                              'district_code': 'I',
                              'inward_code': '0AA'}
            return True
        return False

    def __format_code(self, post_code):
        formatted_val = post_code['area_code'] + post_code['district_code'] +\
                        ' ' + post_code['inward_code']
        return formatted_val

    def validate_postcode(self, s):
        """
        :param s: String to be validated
        :return: Boolean value
        """
        s = s.strip().upper()
        s = re.sub('\s','',s)
        is_special_case = self.__validate_special_case(s)
        if is_special_case:
            return True
        is_valid_case = self.__extract(s)
        if is_valid_case:
            return True
        return False

    def format_postcode(self, s):
        """
        :param s: String to be formatted
        :return: Formatted code if valid, exception if not valid
        """
        if self.validate_postcode(s):
            return self.__format_code(self.post_code)
        else:
            raise ValueError('Invalid postcode cannot be formatted')
















