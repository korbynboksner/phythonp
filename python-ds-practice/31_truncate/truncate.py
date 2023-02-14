def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    np=[]
    if len(phrase) < n:
        print(phrase)
    elif n >= 3:
        for l in phrase:
            np.append(l)
        while n > 0:
            np.pop()
            if len(np) == n-3:
                break
        np.append('.')
        np.append('.')
        np.append('.')
        f = ''.join(np)
        print(f)
    else: 
        print('trunication must be 3 characters')
truncate("Hello World", 6)
truncate("Problem solving is the best!", 10)
truncate("Yo", 100)
truncate("Woah", 3)
truncate('Cool', 1)