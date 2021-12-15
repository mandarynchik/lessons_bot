import hashlib

# hs = hashlib.sha256(get_some_string().encode('utf-8')).hexdigest()

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
 
def check(email):
    if(re.match(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")
        return False


def email_to_hash256(user_email):

    res = hashlib.sha256(user_email.encode('utf-8')).hexdigest()
    return res
    pass

