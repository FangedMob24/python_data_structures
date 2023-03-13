def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_lst = [num for num in str(num1)]
    num2_lst = [num for num in str(num2)]

    num_set = set(num1_lst + num2_lst)

    for num in num_set:
        if num1_lst.count(num) != num2_lst.count(num):
            return False
        
    return True