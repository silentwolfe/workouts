def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
        
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items(), key=lambda item: item[0])

    for key, value in sorted_dict:
        print(f'{key}: {value}')

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)