def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    p = 0
    for i in lst:
        if isinstance(i, (list)):
            None
        else:
            p+=1
    if p==0:
        print(True)
    else: 
        print(False)
