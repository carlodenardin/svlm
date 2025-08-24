def compute_rule_population(rule_value):
    """
    Implements the described algorithm to determine the population count based on a rule value.
    - Input: rule_value (numeric) representing the value of the rule.
    - If rule_value > THRESHOLD, increment the population by INCREMENT until it reaches TARGET (100).
    - Otherwise, decrement the population by DECREMENT until it reaches TARGET (0).
    - Returns the final population value.
    """
    THRESHOLD = 50
    INCREMENT = 10
    DECREMENT = 5
    value = rule_value
    population = 0
    if value > THRESHOLD:
        TARGET = 100
    else:
        TARGET = 0
    max_iters = 1000
    it = 0
    while population != TARGET and it < max_iters:
        if value > THRESHOLD:
            population += INCREMENT
        else:
            population -= DECREMENT
        it += 1
    return population