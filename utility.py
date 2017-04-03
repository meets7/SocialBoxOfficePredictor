import re


def plaintext(movieNameWithAccents):
    movieNameWithAccents = movieNameWithAccents.rstrip()
    movieTitle = re.sub(r'[^ a-zA-Z0-9:-]', '', movieNameWithAccents)
    return movieTitle
