import unittest
from tdd_example import email_to_hash256



class TestHasingEmail(unittest.TestCase):
    def test_strng_to_hashed_string(self):
        email = "egor@gmail.com"
        expected_hash = "8c874bdc5cbfd4fa9d7a76fa18bba18e2149ba126f2ddc58468f7f80c23fdd73" 
        func_res = email_to_hash256(email)
        self.assertEqual(expected_hash, func_res)

    def test_checking_valid_email(self):
        valid_email = "egor@gmail.com"
        invalid_email = "egor"
        expected_hash = "8c874bdc5cbfd4fa9d7a76fa18bba18e2149ba126f2ddc58468f7f80c23fdd73" 
        result_with_valid_email = email_to_hash256(valid_email)
        result_with_invalid_email = email_to_hash256(invalid_email)

        self.assertEqual(expected_hash, result_with_valid_email)
        self.assertEqual(expected_hash, result_with_invalid_email)


unittest.main()
