import sys
import unittest

sys.path.append(".")
from logic.settings import currency_necessary_keys, available_currency_countries
from logic.currencies import currency_message_to_user

NBRB_rb_usd_raw = {'Cur_ID': 431, 'Date': '2021-07-22T00:00:00', 'Cur_Abbreviation': 'USD', 'Cur_Scale': 1, 'Cur_Name': 'Доллар США', 'Cur_OfficialRate': 2.5327}
NBUK_uk_usd_raw = {'r030': 840, 'txt': 'Долар США', 'rate': 27.1915, 'cc': 'USD', 'exchangedate': '23.07.2021'}

uk_abbr = "uk"
rb_abbr = "rb"
unknown = "unknown"

class TestStringMethods(unittest.TestCase):
    def test_raw_currency_to_string_type(self):
        uk_usd_currency_message = currency_message_to_user(NBUK_uk_usd_raw, uk_abbr)
        rb_usd_currency_message = currency_message_to_user(NBRB_rb_usd_raw, rb_abbr)
        empty_raw_input_info = currency_message_to_user({}, rb_abbr)
        #unknown_country_currency_message = currency_message_to_user(NBRB_rb_usd_raw, unknown)

        self.assertTrue(isinstance(uk_usd_currency_message, str))
        self.assertTrue(isinstance(rb_usd_currency_message, str))
        self.assertTrue(isinstance(empty_raw_input_info,bool))

    def test_raw_currency_to_string_value(self):
        expected_currency_message_uk = "Cегодня 1 USD стоит 27.1915 грвн."
        expected_currency_message_rb = "Cегодня 1 USD стоит 2.5327 бел.руб"

        uk_usd_currency_message = currency_message_to_user(NBUK_uk_usd_raw, uk_abbr)
        rb_usd_currency_message = currency_message_to_user(NBRB_rb_usd_raw, rb_abbr)
        empty_raw_input_info = currency_message_to_user({}, rb_abbr)

        self.assertEqual(expected_currency_message_uk, uk_usd_currency_message)
        self.assertEqual(expected_currency_message_rb, rb_usd_currency_message)
        self.assertEqual(empty_raw_input_info, False)


if __name__ == "__main__":
    unittest.main()
