# I am importing json module to work with JSON files
import json


# I am defining a function to read and print JSON file
# fn = file name
# pretty = whether to format nicely (True/False)
# sort = whether to sort keys (True/False)
def read_print_json(fn, pretty, sort):

    # I am opening the JSON file in read mode
    with open(fn, "r") as json_file:

        # I am loading JSON data into Python dictionary
        data = json.load(json_file)

        # I am checking if pretty printing is required
        if pretty:
            # I am printing formatted JSON with sorting and indentation
            print(json.dumps(data, sort_keys=sort, indent=4))
        else:
            # I am printing raw JSON data
            print(data)


# I am defining a function to update JSON data
# fn = file name
# arr_name = array name inside JSON
# pos = position in array
# key = key to update
# value = new value
def update_author_json(fn, arr_name, pos, key, value):

    # I am opening JSON file in read mode
    with open(fn, "r") as read_file:

        # I am loading JSON data
        data = json.load(read_file)

    # I am updating the specific value in JSON
    data[arr_name][pos][key] = value

    # I am opening JSON file in write mode
    with open(fn, "w") as write_file:

        # I am writing updated data back to file
        json.dump(data, write_file, indent=4)


# -------------------- Testing --------------------

# I am reading and printing JSON file
read_print_json("./files_to_read/authors.json", pretty=True, sort=True)

# I am updating JSON file
update_author_json("./files_to_read/authors.json", "authors", 0, "name", "John Doe")
