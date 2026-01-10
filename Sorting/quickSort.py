def quicksort(nums:list):
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    left_partition = [num for num in nums[1:] if num < pivot]
    right_partition = [num for num in nums[1:] if num > pivot]

    return quicksort(left_partition) + [pivot] + quicksort(right_partition)

if __name__ == "__main__":
    print(quicksort([123,10]))

