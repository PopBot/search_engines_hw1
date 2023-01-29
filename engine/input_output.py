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
