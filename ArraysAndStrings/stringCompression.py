#INFO:
# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed7'string would not become smaller than theoriginal string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def string_compression(word:str)->str:
    if len(word) <= 1:
        return word

    count = 0 
    char_in_focus  = word[0]
    #INFO: might be better to use an array since appending at the end is an O(1) task instead of a O(n^2) like the 
    # string concatenation
    compressed_version = ""

    for i in range(len(word)):
        if word[i] == char_in_focus:
            count += 1
        else:
            compressed_version += char_in_focus+str(count)
            char_in_focus = word[i]
            count = 1
    
    compressed_version += char_in_focus+str(count)
    print(compressed_version)
    return compressed_version if len(word) > len(compressed_version) else word






if __name__ == "__main__":
    assert string_compression("aabcccccaaa") == "a2b1c5a3", "you're supposed to get a2blc5a3"
    # Test cases for string compression function

    # Basic compression cases
    assert string_compression("aabcccccaaa") == "a2b1c5a3", "Basic compression with multiple repeated chars"
    assert string_compression("aaa") == "a3", "Single character repeated"
    assert string_compression("aaabbb") == "a3b3", "Two different characters repeated"

    # Edge cases - no compression benefit
    assert string_compression("abc") == "abc", "No repeated chars - return original"
    assert string_compression("abcd") == "abcd", "All different chars - return original"
    assert string_compression("ab") == "ab", "Two different chars - return original"
    assert string_compression("aabb") == "aabb", "Compression same length as original - return original"

    # Single character cases
    assert string_compression("a") == "a", "Single character - return original"
    assert string_compression("aa") == "aa", "Two same chars - compression not beneficial"

    # Empty string
    assert string_compression("") == "", "Empty string should return empty"

    # Mixed case scenarios
    assert string_compression("AAAaaa") == "A3a3", "Uppercase and lowercase are different"
    assert string_compression("aAbBcC") == "aAbBcC", "Alternating case - return original"
    assert string_compression("AAaaBBbb") == "AAaaBBbb", "Mixed case pairs - return original"

    # Long compression scenarios
    assert string_compression("aaaaaaaaaa") == "a10", "Ten repeated characters"
    assert string_compression("aabbccddee") == "aabbccddee", "All pairs - return original"
    assert string_compression("aaabbbcccddd") == "a3b3c3d3", "Multiple groups of three"

    # Complex patterns
    assert string_compression("abcabcabc") == "abcabcabc", "Repeating pattern - return original"
    assert string_compression("aaabaaabaaab") == "aaabaaabaaab", "Complex pattern - return original"
    assert string_compression("aabbbaabbbaaa") == "a2b3a2b3a3", "Mixed pattern - return original"
    assert string_compression("aaaabbbbccccdddd") == "a4b4c4d4", "Four groups of four"

    # Edge cases with single occurrences mixed with repetitions
    assert string_compression("aabbcc") == "aabbcc", "All pairs - return original"
    assert string_compression("aaabcd") == "aaabcd", "Mixed single and multiple - return original"
    assert string_compression("abcccdef") == "abcccdef", "One group in middle - return original"
    assert string_compression("aabbbccccdddddeeeee") == "a2b3c4d5e5", "Increasing repetitions"

    # Large repetition counts
    assert string_compression("a" * 100) == "a100", "Very long repetition"
    assert string_compression("a" * 50 + "b" * 50) == "a50b50", "Two very long repetitions"

    # Boundary cases for compression effectiveness
    assert string_compression("aabbccdd") == "aabbccdd", "Four pairs - not beneficial"
    assert string_compression("aaabbbccc") == "a3b3c3", "Three groups of three - beneficial"
