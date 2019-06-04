match_string = "Apple"
get_matching_indices = [i for i, x in enumerate(list(mylist)) if len(x) == 1 and x[0] == match_string]
