NUM_CHARS = 26

def print_sorted_strings_main(remaining):
    import pdb; pdb.set_trace()
    print_sorted_strings(remaining,"")

def print_sorted_strings(remaining, prefix=""):
    if remaining == 0:
        if is_in_order(prefix):
            print(prefix)
    else:
        for i in range(NUM_CHARS):
            c = ith_letter(i)
            print_sorted_strings(remaining - 1, prefix + c)

def is_in_order(s):
    for i in range(1, len(s)):
        prev = ord(s[i - 1]) - ord('a')
        curr = ord(s[i]) - ord('a')
        if prev > curr:
            return False
    return True

def ith_letter(i):
    return chr(ord('a') + i)

if __name__ == "__main__":
    print_sorted_strings_main(2)    
