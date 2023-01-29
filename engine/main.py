from scraping import SearchEngine
from input_output import *
import logging
import os


FILE = "100QueriesSet2.txt"


def main():
    output_absolute_file_path = os.path.join(os.path.dirname(__file__) + "/results.json")
    file_path = get_absolute_file_path_for_relative_file(FILE)
    results = {}
    queries = read_file_line_by_line(file_path)
    for query in queries:
        results[query] = SearchEngine.search(query)
    write_dict_to_json_file(output_absolute_file_path, results)
    logging.info("Done!")


def test():
    query = 'chicken'
    results = SearchEngine.search(query)
    print(results)
    res = {query: results}
    output_absolute_file_path = os.path.join(os.path.dirname(__file__) + "/results.json")
    write_dict_to_json_file(output_absolute_file_path, res)


if __name__ == '__main__':
    test()
