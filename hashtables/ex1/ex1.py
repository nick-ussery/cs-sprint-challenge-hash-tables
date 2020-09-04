def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weights_dict = {}
    for weight in weights:  # create dict of possible solutions based off each weight
        if weight not in weights_dict:
            weights_dict[weight] = limit-weight

    for weight in weights_dict.items():  # loop through looking for the solution pairs
        # print(weight)
        if len(weights) == 2:  # if there are only 2 weights then return them reversed
            result = [len(weights) - 1 - weights[::-
                                                 1].index(weights[1]), weights.index(weight[1])]
            return result
        if weight[1] in weights:  # returns the solution pair by finding index of each
            return [weights.index(weight[1]), weights.index(weights_dict[weight[1]])]

    return None  # base case, no solutions
