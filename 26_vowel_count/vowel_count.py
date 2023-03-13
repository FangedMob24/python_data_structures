def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel = ('o','a','e','u','i')
    low_case = phrase.lower()

    counted = {n : low_case.count(n) for n in low_case if n in vowel and low_case.count(n) > 0}

    return counted