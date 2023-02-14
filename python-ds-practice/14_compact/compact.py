def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    true = []
    for e in lst:
        if(bool(e)):
            true.append(e)
    print(true)
compact([0, 1, 2, '', [], False, (), None, 'All done'])