# INFO:
# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
# pbale, pale => abelp,aelp


# pice, pice


#INFO: works but there's one bad case where it will fail
#fails on this case
# print(one_away("abc", "axcy"))

def one_away(string_one, string_two):
    if abs(len(string_one) - len(string_two)) > 1:
        return False

    one_diff_found = False

    if len(string_one) == len(string_two):
        for i in range(len(string_one)):
            if string_one[i] != string_two[i]:
                if one_diff_found:
                    return False
                one_diff_found = True
    #INFO: I could have made this a function and then called it with switched up input 
    #INFO: I could have done ternary operators also to find which string was the longest or shortest 
    else:
        if len(string_one) > len(string_two):
            for i in range(len(string_two)):
                print(string_two[i])
                if (string_two[i]) != (string_one[i]):
                    if one_diff_found:
                        return False
                    if (string_two[i]) != (string_one[i + 1]):
                        one_diff_found = True

        else:
            for i in range(len(string_one)):
                if (string_one[i]) != (string_two[i]):
                    if one_diff_found:
                        return False
                    if (string_one[i]) != (string_two[i + 1]):
                        one_diff_found = True

    return True

def one_away_optimized(one:str, two:str)-> bool:
    if abs(len(one) - len(two)) > 1:
        return False

    if len(one) == len(two):
        return one_edit_replace(one,two)
    elif len(one)-len(two) == 1:
        return one_edit_insert(one,two)
    else:
        return one_edit_insert(two,one)



def one_edit_replace(one:str,two:str)-> bool:
    one_diff_found = False

    for i in range(len(one)):
        if one[i] != two[i]:
            if one_diff_found:
                return False
            one_diff_found = True

    return True

def one_edit_insert(one:str,two:str) -> bool:
    #two is the shorter one
    index1 = 0
    index2 = 0
    while index1 < len(one) and index2 < len(two):
        if two[index2] != one[index1]:
            if(index1 != index2):
                return False
            index1 += 1
        else:
            index2 += 1 
            index1 += 1
    return True



if __name__ == "__main__":
    assert one_away_optimized("abc","axcy") == False, "they shouldn't be one away"

    # ✅ Replacement cases
    assert one_away_optimized("cat", "cut") == True, "one replacement in middle"
    assert one_away_optimized("cat", "cast") == True, "insertion near end"
    assert one_away_optimized("cat", "cats") == True, "insertion at end"
    assert one_away_optimized("cat", "at") == True, "removal at start"
    assert one_away_optimized("cat", "ca") == True, "removal at end"
    assert one_away_optimized("cat", "dog") == False, "three replacements needed"
    assert one_away_optimized("abcd", "abxd") == True, "replacement in middle"
    assert one_away_optimized("abcd", "axcd") == True, "replacement near start"

    # ✅ Insertion / Removal at beginning
    assert one_away_optimized("abc", "aabc") == True, "insertion at start"
    assert one_away_optimized("aabc", "abc") == True, "removal at start"
    assert one_away_optimized("abc", "zabc") == True, "insertion at very beginning"
    assert one_away_optimized("zabc", "abc") == True, "removal at very beginning"

    # ✅ Insertion / Removal in middle
    assert one_away_optimized("abcd", "abxcd") == True, "insertion in middle"
    assert one_away_optimized("abxcd", "abcd") == True, "removal in middle"
    assert one_away_optimized("abcdef", "abdef") == True, "removal of middle char"
    assert one_away_optimized("abdef", "abcdef") == True, "insertion of middle char"

    # ✅ Insertion / Removal at end
    assert one_away_optimized("abc", "abcd") == True, "insertion at end"
    assert one_away_optimized("abcd", "abc") == True, "removal at end"
    assert one_away_optimized("abc", "abcc") == True, "insertion duplicate at end"
    assert one_away_optimized("abcc", "abc") == True, "removal duplicate at end"

    # ✅ Zero edits
    assert one_away_optimized("xyz", "xyz") == True, "identical strings"
    assert one_away_optimized("", "") == True, "both empty strings"

    # ✅ Edge cases with empty strings
    assert one_away_optimized("", "a") == True, "empty vs one char"
    assert one_away_optimized("a", "") == True, "one char vs empty"
    assert one_away_optimized("", "ab") == False, "empty vs two chars"
    assert one_away_optimized("ab", "") == False, "two chars vs empty"

    # ✅ Multiple edits (should fail)
    assert one_away_optimized("abc", "axcy") == False, "two edits in different places"
    assert one_away_optimized("kitten", "sitting") == False, "classic edit distance > 1"
    assert one_away_optimized("pale", "bake") == False, "two replacements apart"
    assert one_away_optimized("abcd", "wxyz") == False, "completely different"

    # ✅ Longer tricky cases
    assert one_away_optimized("abcdefgh", "abcxefgh") == True, "one replacement in long string"
    assert one_away_optimized("abcdefgh", "abcdxefgh") == True, "one insertion in long string"
    assert one_away_optimized("abcdefgh", "abcdfgh") == True, "one removal in long string"
    assert one_away_optimized("abcdefgh", "abxyefgh") == False, "two edits in long string"

