# INFO:
# Question Title: Check Permutation
# Question: Given two strings write a method to check if one is a permutation of the other


def checkPermutation(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    count = [0] * 128

    for char in str_1:
        count[ord(char)] += 1
    for char in str_2:
        count[ord(char)] -= 1

    return sum(count) == 0


if __name__ == "__main__":
    assert (
        checkPermutation("kwabena", "none") == False
    ), "kwabena should not be a permutation to none"
    assert (
        checkPermutation("kwabena", "wabenak") == True
    ), "kwabena and wabenak are a permutation of each other"

# Example:
# "kwabena" "wabenak"
