import random
import string

if __name__ == '__main__':

    random_dicts_list = []
    num_dicts = random.randint(2, 10)  # Random number of dictionaries in the list

    for _ in range(num_dicts):
        num_keys = random.randint(1, 10)  # Random number of keys
        keys = random.sample(string.ascii_lowercase, num_keys)  # Random letters as keys
        values = [random.randint(0, 100) for _ in range(num_keys)]

        random_dicts_list.append(dict(zip(keys, values)))  # Combine keys and values into a dictionary

    print(random_dicts_list)

    merged_dict = {}
    for i in range(len(random_dicts_list)):  # merges all dictionaries in one
        dct = random_dicts_list[i]
        for x in dct.keys():
            merged_dict[f"{x}_{i + 1}"] = dct[x]  # adds index(it means the dictionary number in the list) to the key
    print(merged_dict)

    filtered_dict = {}
    for k in merged_dict:  # sorts the dictionary by selecting the greatest value for each key-letter
        common_key = k[0]
        common_dict = {key: val for key, val in merged_dict.items() if key.startswith(common_key)}
        if len(common_dict) == 1:
            value = common_dict.get(k)
            common_dict.clear()
            common_dict[common_key] = value
        sorted_common_dict = sorted(common_dict.items(), key=lambda x: x[
            1])  # sorts the items of common_dict and assigns the result to sorted_common_dict
        max_key_value = list(sorted_common_dict)[
            -1]  # extracts the last (maximum) item from the sorted list and assigns it to max_key_value
        filtered_dict[max_key_value[0]] = max_key_value[1]
    print(filtered_dict)
