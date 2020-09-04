def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # need to turn each list into a dict, then count the nums in each list. only if a num exists in all lists is it an intersection
    num_arrays = len(arrays)

    num_dict = {}  # this is the list of all nums and how many times they were seen
    for array in arrays:  # cycle through array of arrays
        for i in array:  # cycle through individual array
            if i not in num_dict:  # is num in the dict yet, if not, add it
                num_dict[i] = 0
            num_dict[i] += 1
    # now to find the numbers that have counter == #of arrays
    result = []

    for nums in num_dict.items():  # go through all values in dictionary finding the numbers that are in each array
        if nums[1] == num_arrays:
            result.append(nums[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
