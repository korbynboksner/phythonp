def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    t=0
    i=0
    if start==0:  
        while i < len(nums):
            t+=nums[i]
            i+=1
    else:
        i=start
        while i <len(nums):
            t+=nums[i]
            i+=1
    print(t)

nums = [1, 2, 3, 4]
sum_range(nums, 1)
sum_range(nums)