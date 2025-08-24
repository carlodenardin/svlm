def remove_k_largest(l: list[int], k: int) -> list[int]:
    l.sort()
    return l[:-k]