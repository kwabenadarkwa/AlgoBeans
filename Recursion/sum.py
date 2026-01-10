import math
def count(nums:list)->int:
    if nums == []: 
        return 0
    return 1 + count(nums[1:])

def sum(nums:list)->int:
    if nums == []:
        return 0
    return nums[0] + sum(nums[1:])
    #TODO: look at what they did in the book here

def max_num_in_list(nums):
    if len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    sub_max = max(nums[1:])
    return nums[0] if nums[0] > sub_max else sub_max

# def max_num_in_list(nums:list)-> int:
#     return max_thing(nums,nums[0])
#
# def max_thing(nums,max)->int:
#    if nums == []:
#         return max
#
#    if nums[0] > max:
#         max = nums[0]
#
#    return max_thing(nums[1:],max)
#
if __name__ == "__main__":
    # print(sum([1,2,3,4,10]))
    print(max_num_in_list([200,2,3,4,51,2000]))
    # print(count([1,2,3,4,5]))

