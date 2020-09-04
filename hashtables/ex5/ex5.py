# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create a dict of the paths
    # then find if the queries exist in the paths
    # return the paths that are in the queries
    paths_dict = {}

    for path in files:  # grab the filename from each path cause thats what we are searching for
        name = path.split('/')[-1]
        if name not in paths_dict:  # check if file is in the dict yet
            paths_dict[name] = []
        paths_dict[name].append(path)  # add the path to the dict

    # dict created. now to go through queries and find the paths
    result = []
    for query in queries:  # cycle through queries
        if query in paths_dict:  # if the query is in the dict. that means we have it, add it
            result.extend(paths_dict[query])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
