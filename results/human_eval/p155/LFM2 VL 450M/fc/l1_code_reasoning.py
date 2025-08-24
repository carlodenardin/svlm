import sys

def count_even_odd_digits(n: int):
    m = abs(int(n))
    s = str(m)
    count_e = sum((1 for ch in s if (ord(ch) - ord('0')) % 2 == 0))
    count_o = len(s) - count_e
    step3_e = 0
    step3_o = 0
    for ch in s:
        d = ord(ch) - ord('0')
        if d % 2 == 0:
            for ch2 in str(d):
                if (ord(ch2) - ord('0')) % 2 == 0:
                    step3_e += 1
                else:
                    step3_o += 1
    step4_e = 0
    step4_o = 0
    for ch in s:
        d = ord(ch) - ord('0')
        if d % 2 == 1:
            for ch2 in str(d):
                if (ord(ch2) - ord('0')) % 2 == 0:
                    step4_e += 1
                else:
                    step4_o += 1
    return (count_e, count_o)