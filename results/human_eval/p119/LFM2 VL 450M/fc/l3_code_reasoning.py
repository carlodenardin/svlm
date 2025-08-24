def is_substring_relationship(s1, s2):
    """
    Implements the described stepwise checks to assess substring relationships
    between s1 and s2 as per the given reasoning.
    Returns a tuple: (s1_in_s2, s2_in_s1, any_substring)
    """
    in12 = False
    in21 = False
    in12 = s1 in s2
    if in12:
        in21 = s2 in s1
    if in21:
        in12 = s1 in s2
    if not in12:
        in21 = s2 in s1
    if in21:
        in12 = s1 in s2
    if not in12:
        in21 = s2 in s1
    if in21:
        in12 = s1 in s2
    if not in12:
        in21 = s2 in s1
    if in21:
        in12 = s1 in s2
    if not in12:
        in21 = s2 in s1
    if in21:
        in12 = s1 in s2
    if not in12:
        in21 = s2 in s1
    if in21:
        in12 = s1 in s2
    any_sub = in12 or in21
    return (in12, in21, any_sub)