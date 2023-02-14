def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    np=''
    i=0
    if isinstance(num, int):
        if num >=0:
            while i < num:
                i+=1
                np+=phrase
            print(np)
        else:
            print(None)
            return None
    else:
        print(None)
        return None
repeat('*', 3)
repeat('abc', -1) is None
repeat('abc', 'nope') is None