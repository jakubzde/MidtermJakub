import re

def is_valid_url(url):
    regex_pattern = r"^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$"
    if re.match(regex_pattern, url):
        return True
    else:
        return False
    
url = "https://email.seznam.cz/?i&q=label-id%3A258"
print(is_valid_url(url))