import random
import string

def create_random_dicts_list() -> list:
    """
        returns list of dictionaries
        """
    random_dicts_list = []
    num_dicts = random.randint(2, 10)

    for _ in range(num_dicts):
        num_keys = random.randint(1, 10)
        keys = random.sample(string.ascii_lowercase, num_keys)
        values = [random.randint(0, 100) for _ in range(num_keys)]

        random_dicts_list.append(dict(zip(keys, values)))

    return random_dicts_list


def merge_all_dicts(list_of_dicts: list) -> dict:
    """
        takes in list of dictionaries, merges all dictionaries in one, adds index if needed
        returns merged dictionary
        """
    merged_dict = {}
    for i in range(len(list_of_dicts)):
        dct = list_of_dicts[i]
        for x in dct.keys():
            merged_dict[f"{x}_{i + 1}"] = dct[x]
    print(merged_dict)
    return merged_dict


def filter_dict(merged_dict: dict) -> dict:
    """
        takes in dictionary, sorts the dictionary by selecting the greatest value for each key-letter
        returns merged dictionary
        """
    filtered_dict = {}
    for k in merged_dict:
        common_key = k[0]
        common_dict = {key: val for key, val in merged_dict.items() if key.startswith(common_key)}
        if len(common_dict) == 1:
            value = common_dict.get(k)
            common_dict.clear()
            common_dict[common_key] = value
        sorted_common_dict = sorted(common_dict.items(), key=lambda x: x[
            1])
        max_key_value = list(sorted_common_dict)[
            -1]
        filtered_dict[max_key_value[0]] = max_key_value[1]
    print(filtered_dict)
    return filtered_dict


if __name__ == '__main__':
    list_of_dictionaries = create_random_dicts_list()
    print(list_of_dictionaries)
    joined_dict = merge_all_dicts(list_of_dictionaries)
    filter_dict(joined_dict)
