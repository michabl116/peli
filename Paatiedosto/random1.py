import random
dictionary_A = {
    'key1': -40,
    'key2': 50,
    'key3': 20,
    'key4': 100,
    'key5': 500,
    'key6': 1000,
}


def get_random_value_as_int():
    random_key = random.choice(list(dictionary_A.keys()))
    value = dictionary_A[random_key]

    if isinstance(value, (int, float)):
        return int(value)





