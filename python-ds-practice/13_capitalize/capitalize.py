def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    f = phrase[0].upper() + phrase[1:]
    print(f)
   
capitalize('python')
capitalize('only first word')