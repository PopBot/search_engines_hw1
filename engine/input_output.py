import json
import os


def read_file_line_by_line(absolute_file_path) -> list[str]:
    # Given an absolute file path, read the file line by line
    # absolute_file_path is a string
    # returns a list of strings
    with open(absolute_file_path, 'r') as f:
        lines = f.readlines()
        f.close()
        return lines


def write_dict_to_json_file(absolute_file_path, dictionary):
    # Given an absolute file path and a dictionary, write the dictionary to the file
    # absolute_file_path is a string
    # dictionary is a dictionary
    with open(absolute_file_path, 'w') as f:
        json.dump(dictionary, f, indent=4)
        f.close()


def get_absolute_file_path_for_relative_file(file_name):
    # Given a file name, return the absolute file path for the file
    # file_name is a string
    # returns a string
    return os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))


def open_json_file_and_append_json(absolute_file_path, dict_json_to_append):
    if not os.path.isfile(absolute_file_path):
        with open(absolute_file_path, 'w') as f:
            json.dump(dict_json_to_append, f, indent=4)
            f.close()
    else:
        with open(absolute_file_path, 'r') as f:
            data = json.load(f)
            # Check if there is already a key with the same name
            for key in dict_json_to_append.keys():
                if key in data.keys():
                    return
            data.update(dict_json_to_append)
            with open(absolute_file_path, 'w') as wr:

                json.dump(data, wr, indent=4)
                wr.close()
            f.close()
    print("Done!")


def batch_read_file_line_by_line(absolute_file_path: str, limit: int, offset: int) -> list[str]:
    # Given an absolute file path, read the file line by line
    # absolute_file_path is a string
    # returns a list of strings
    with open(absolute_file_path, 'r') as f:
        lines = f.readlines()
        f.close()
        return lines[offset:offset + limit]


def batch_process_file_line_by_line(absolute_file_path: str, count_per_page: int) -> list[list[str]]:
    # Given an absolute file path, read the file line by line
    # absolute_file_path is a string
    # returns a list of strings
    with open(absolute_file_path, 'r') as f:
        lines = f.readlines()
        f.close()
        # Remove the ' \n' at the end of each line
        lines = [line.rstrip() for line in lines]
        return [lines[i:i + count_per_page] for i in range(0, len(lines), count_per_page)]
        # return [lines[i:i + count_per_page] for i in range(0, len(lines), count_per_page)]


def count_number_of_items_in_multidimensional_list(list_to_count: list[list[str]]) -> int:
    count = 0
    for page in list_to_count:
        count += len(page)
    return count
