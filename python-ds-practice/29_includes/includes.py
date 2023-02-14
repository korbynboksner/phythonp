def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if isinstance(collection, (list, tuple, str)):
        if start==None:
            i=0
        else:
            i=start
        while i < len(collection):
            if collection[i] == sought:
                print(True)
                break
            else:
                i += 1
                if i ==len(collection):
                    print(False)
                    break
    if isinstance(collection, set):
        t =set()
        for n in collection:
            if n==sought:
                print(True)
                break
            else:
                t.add(n)
                if t == collection:
                    print(False)
            


includes([1, 2, 3], 1, 2)
includes("hello", "o")
includes(('Elmo', 5, 'red'), 'red', 1)


includes({1, 2, 3}, 4, 3)  



