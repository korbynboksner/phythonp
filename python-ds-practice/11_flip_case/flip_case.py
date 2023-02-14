def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    k = []
    
    
    if to_swap.isupper():
        for c in phrase:
            if c == to_swap: 
                l = to_swap.lower()
                k.append(l)
            elif c == to_swap.lower():
                u = to_swap.upper()
                k.append(u)
            else:
                k.append(c)
    else:
        for c in phrase:
            if c == to_swap: 
                l = to_swap.upper()
                k.append(l)
            elif c == to_swap.upper():
                u = to_swap.lower()
                k.append(u)
            else:
                k.append(c)    
    print("".join(k))
    
        

        #f = phrase.replace(to_swap,to_swap.lower())
        #l = f.replace(to_swap.lower(),to_swap)
        #print(l)
flip_case('Aaaahhh', 'h')