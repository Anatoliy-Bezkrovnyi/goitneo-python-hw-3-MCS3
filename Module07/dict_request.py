def make_request(keys, values):
    res_dictionary = dict()
    if len(keys) != len(values):
        return res_dictionary
    else:
        counter = 0
        while counter != len(keys):
            res_dictionary[keys[counter]] = values[counter]
            counter = counter + 1
        return res_dictionary