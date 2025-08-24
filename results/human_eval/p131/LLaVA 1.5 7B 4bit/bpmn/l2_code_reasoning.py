def compute_product_of_odd_digits(number: int, odd_digits=None) -> int:
    """
    Implements the described algorithm:
    - Initialize a product variable (implicitly 1).
    - Iterate through the list of odd digits in order.
    - For each digit, multiply the current product by the digit.
    - If the digit is not the last in the list, add the digit to the product.
    - If the digit is the last, return the product (without additional addition).

    Parameters:
    - number: The input integer. If odd_digits is not provided, its digits are scanned to
              form the list of odd digits.
    - odd_digits: Optional list of odd digits to process in order. If provided, it is used
                  directly (after ensuring it's a list of integers). If None, odd digits are
                  derived from 'number'.

    Returns:
    - The final computed product according to the described flow.
    """
    if odd_digits is None:
        n = abs(int(number))
        digits = [int(ch) for ch in str(n)]
        odd_digits = [d for d in digits if d % 2 == 1]
    else:
        odd_digits = [int(d) for d in odd_digits if int(d) % 2 == 1]
    if not odd_digits:
        return 0
    product = 1
    total = len(odd_digits)
    for idx, d in enumerate(odd_digits):
        d = int(d)
        product *= d
        if idx == total - 1:
            return product
        else:
            product += d