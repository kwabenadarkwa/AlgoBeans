# INFO:
# Question Title: Is Unique
# Question: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def is_unique_additional_data_structures(s):
    string_len = len(s)
    set_of_chars = set()

    for char in s:
        set_of_chars.add(char)

    return string_len == len(set_of_chars)


def is_unique_without_data_structures(s):

    ascii_count = 128
    count = [0] * ascii_count
    #could also use an array of booleans. I guess if we want to go deep into it that could be better

    for char in s:
        if(count[ord(char)] == 1):
            return False
        else:
            count[ord(char)] += 1

    return True


if __name__ == "__main__":
    assert is_unique_additional_data_structures("from") == True, "one case failed"
    assert is_unique_additional_data_structures("topic") == True, "another one failed"
    assert is_unique_additional_data_structures("meet") == False, "failed"
    assert is_unique_additional_data_structures("pleet") == False, "failed"


    assert is_unique_without_data_structures("from") == True, "one case failed"
    assert is_unique_without_data_structures("topic") == True, "another one failed"
    assert is_unique_without_data_structures("meet") == False, "failed"
    assert is_unique_without_data_structures("pleet") == False, "failed"



# Example: "kwabena"
# Test Cases
# from
# topic
# meet
# pleet
