def concatenate_strings(strings):
    combined_strings = ""
    for string in strings:
        combined_strings += string
    return combined_strings

def check_combinations(combined_strings):
    if len(combined_strings) == len(combined_strings[1:]):
        return True
    else:
        return False

def main():
    strings = ["abc", "def", "ghi"]
    combined = concatenate_strings(strings)
    if check_combinations(combined):
        print("Return No if both the combinations are unbalanced, 'Yes' otherwise")
    else:
        print("Return No if both the combinations are unbalanced, 'Yes' otherwise")

if __name__ == "__main__":
    main()