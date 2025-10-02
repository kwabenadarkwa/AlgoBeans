# INFO:
# Question Title: Palindrome Permutation
# Question:Given a string, write a function to check if it is a permutation of apalindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)


def palindrome_permutation(s):
    s = s.lower()
    ascii_char_count = 128
    count_odd = False
    char_count = [0] * ascii_char_count

    for char in s:
        if char != " ":
            char_count[ord(char)] += 1
        else:
            continue

    for num in char_count:
        if num % 2 == 1:
            if count_odd:
                return False
            count_odd = True

    return True


if __name__ == "__main__":
    assert (
        palindrome_permutation("Tact Coa") == True
    ), "Tact Coa should be a palindrome permutation"

    assert (
        palindrome_permutation("elvel") == True
    ), "level should be a palindrome permutation"

    assert palindrome_permutation("kwabena") == False, "kwabena isn't "
    assert palindrome_permutation("noon") == True, "mama isn't "
    assert (
        palindrome_permutation("aaabbb") == False
    ), "this should be a palindrome permutation"
