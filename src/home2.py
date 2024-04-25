import random
import string


# lst = [{"a": 1, "b": 2}, {"a": 3, "b": 0}, {"a": 4, "b": 0, "c": 7, }]
def create_random_dicts_list():
    random_dicts_list = []
    num_dicts = random.randint(2, 10)

    for _ in range(num_dicts):
        num_keys = random.randint(1, 10)
        keys = random.sample(string.ascii_lowercase, num_keys)
        values = [random.randint(0, 100) for _ in range(num_keys)]

        random_dicts_list.append(dict(zip(keys, values)))

    return random_dicts_list


# method that merges two dictionaries and adds index(means the dictionary number in the list) to the key
def merge_two_dicts(main_dct, dict2, index):
    for i in dict2.keys():
        main_dct[f"{i}-{index + 1}"] = dict2[i]
    return main_dct


def merge_all_dicts(list_of_dicts):
    merged_dict = {}
    for i in range(len(list_of_dicts)):  # merges all dictionaries in one
        dct = list_of_dicts[i]
        merged_dict = merge_two_dicts(merged_dict, dct, i)
    print(merged_dict)
    return merged_dict


def filter_dict(merged_dict):
    filtered_dict = {}
    for k in merged_dict:  # sorts the dictionary by selecting the greatest value for each key-letter
        common_key = k[0]
        common_dict = {key: val for key, val in merged_dict.items() if key.startswith(common_key)}
        sorted_common_dict = sorted(common_dict.items(), key=lambda x: x[1])
        max_key_value = list(sorted_common_dict)[-1]
        filtered_dict[max_key_value[0]] = max_key_value[1]
    print(filtered_dict)


if __name__ == '__main__':
    list_of_dictionaries = create_random_dicts_list()   # Generate a list of random number of dicts
    print(list_of_dictionaries)
    joined_dict = merge_all_dicts(list_of_dictionaries)
    filter_dict(joined_dict)
