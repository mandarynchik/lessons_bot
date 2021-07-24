import unittest

available_currency_countries = ("uk","rb")
currency_necessary_keys = {"uk": ('txt', 'rate', 'cc', 'exchangedate'),
                           "rb": ('Date', 'Cur_Abbreviation', 'Cur_Scale', 'Cur_Name', 'Cur_OfficialRate')}


NBRB_rb_usd_raw = {'Cur_ID': 431, 'Date': '2021-07-22T00:00:00', 'Cur_Abbreviation': 'USD', 'Cur_Scale': 1, 'Cur_Name': 'Доллар США', 'Cur_OfficialRate': 2.5327}
NBUK_uk_usd_raw = {'r030': 840, 'txt': 'Долар США', 'rate': 27.1915, 'cc': 'USD', 'exchangedate': '23.07.2021'}


uk_abbr = "uk"
rb_abbr = "rb"

def currency_message_to_user(today_currency_info:dict, country_abbr:str):
    if type(today_currency_info) == dict:
        for key in currency_necessary_keys[country_abbr]:
            if key not in today_currency_info.keys():
                return False

        if country_abbr == "rb":
            money_abbr = today_currency_info['Cur_Abbreviation']
            country_money = "бел.руб"
            rate = today_currency_info["Cur_OfficialRate"]
            scale = today_currency_info["Cur_Scale"]

        if country_abbr == "uk":
            money_abbr = today_currency_info['cc']
            country_money = "грвн."
            rate = today_currency_info["rate"]
            scale = 1

        message = f"Cегодня {scale} {money_abbr} стоит {rate} {country_money}"
        return message
    else:
        error_message = f"Some troubles with request to {updates_url}: {e}"
        logger.error(error_message)

uk_raw_to_message = currency_message_to_user(NBUK_uk_usd_raw, uk_abbr)
rb_raw_to_message = currency_message_to_user(NBRB_rb_usd_raw, rb_abbr)

#print(uk_raw_to_message)
#print(rb_raw_to_message)


class TestStringMethods(unittest.TestCase):
    def test_raw_currency_to_string_type(self):
        uk_usd_currency_message = currency_message_to_user(NBUK_uk_usd_raw, uk_abbr)
        rb_usd_currency_message = currency_message_to_user({}, rb_abbr)

        self.assertTrue(isinstance(uk_usd_currency_message, str))
        self.assertTrue(isinstance(rb_usd_currency_message, bool))
    
    def test_raw_currency_to_string_value(self):
        uk_usd_currency_message = currency_message_to_user(NBUK_uk_usd_raw, uk_abbr)
        rb_usd_currency_message = currency_message_to_user(NBRB_rb_usd_raw, rb_abbr)

        expected_currency_message_uk = "Cегодня 1 USD стоит 27.1915 грвн."
        expected_currency_message_rb = "Cегодня 1 USD стоит 2.5327 бел.руб"

        self.assertEqual(expected_currency_message_uk, uk_usd_currency_message)
        self.assertEqual(expected_currency_message_rb, rb_usd_currency_message)
    

if __name__ == "__main__":
    unittest.main()
