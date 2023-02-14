def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    f = dict()
    s = set(phrase)
    for char in s:
        f[f"{char}"]= f"{phrase.count(char)}"
    print(f)
    return f
multiple_letter_count('Yay')