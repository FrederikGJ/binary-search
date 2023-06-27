def find_rotation_point(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = low + (high - low) // 2

        # If the mid element is greater than the high element,
        # the smallest element is in the right half of the array
        if nums[mid] > nums[high]:
            low = mid + 1

        # Else, the smallest element is in the left half of the array
        else:
            high = mid

    # When low and high meet, they point to the smallest element (rotation point)
    return low

# Creating a list of numbers from 1 to 100
nums = list(range(1, 101))

rotation_point_index = 77
nums = nums[rotation_point_index:] + nums[:rotation_point_index]

print("\n The list of numbers with a rotation point is as follows \n")
print(nums, "\n")

rotation_point = find_rotation_point(nums)

print("Rotation point is at index:", rotation_point, "\n")
