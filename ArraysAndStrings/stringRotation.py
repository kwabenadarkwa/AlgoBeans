# INFO:
# Question Title: String Rotation
# Question:Assume you have a method isSubstring which checks if one word is a substring
#of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
# EXAMPLE
#(e.g., "waterbottle" is a rotation of "erbottlewat")

def is_string_rotation(s1:str,s2:str)->bool:
    if(len(s1) != len(s2)):
        return False

    return is_substring(s1+s1,s2) 

def is_substring(string, sub):
    return string.find(sub) != -1

if __name__ == "__main__":
    print(is_string_rotation("erbottlewat","waterbottle"))

