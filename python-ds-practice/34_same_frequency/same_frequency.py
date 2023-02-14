def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    sn1=str(num1)
    sn2=str(num2)
    d1={}
    d2={}
    for n in sn1:
        b = sn1.count(n)
        if b > 0:
            d1[n] = b
    for n in sn2:
        b = sn2.count(n)
        if b > 0:
            d2[n] = b
    if d1 == d2:
        print(True)
    else:
        print(False)
same_frequency(551122, 221515)
same_frequency(321142, 3212215)
same_frequency(1212, 2211)