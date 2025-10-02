# INFO:
# Question Title: URLify
# Question: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to 
# hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr Dohn Smith ", 13
# Output: "Mr%22John%2QSmith"


def urlify(string,length):
    #brute force cheating solution
    # new_str = string.strip()
    # new_str = new_str.replace(" ","%20")
    # return new_str

    replacement_value = "%20"
    new_length = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            string[new_length - 3: new_length] = replacement_value
            new_length -= 3
        else:
            string[new_length - 1] = string[i]
            new_length -= 1
    return string


if __name__ == "__main__":
    print(urlify(list("much ado about nothing      "),22))



