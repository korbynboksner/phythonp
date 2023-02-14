def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    caps= []
    lower_phrase=phrase.lower()
    p = lower_phrase.split()
    for l in p:
        n = l[0].upper() + l[1:]
        caps.append(n)
    final =' '.join(caps)
    print(final)


titleize('this is awesome')
titleize('oNLy cAPITALIZe fIRSt')