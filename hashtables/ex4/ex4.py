def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # return only the positive integers that have a negative match
    # create  a dict that keeps each entry in the list
    # then find the pairs

    num_dict = {}

    for i in a:
        if i not in num_dict:
            num_dict[i] = None  # must establish as none until pair is found
    # now dict is made, need to find the pairs
    result = []
    for nums in num_dict.items():
        if nums[0] > 0:  # only check positive
            if (-nums[0]) in num_dict:  # find the negative
                result.append(nums[0])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
