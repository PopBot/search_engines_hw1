from scraping import SearchEngine
from input_output import *
import logging
import os


FILE = "100QueriesSet2.txt"

output_absolute_file_path = os.path.join(os.path.dirname(__file__) + "/results.json")

file_path = get_absolute_file_path_for_relative_file(FILE)


def main():
    results = {}
    queries = read_file_line_by_line(file_path)
    for query in queries:
        results[query] = SearchEngine.search(query)
        print(results[query])
    write_dict_to_json_file(output_absolute_file_path, results)
    logging.info("Done!")


def test():
    query = 'chicken'
    results = SearchEngine.search(query)
    print(results)
    res = {query: results}

    write_dict_to_json_file(output_absolute_file_path, res)


def test_2():
    print("test_2")
    print(batch_process_file_line_by_line(file_path, 10))


def run():
    # res = {}
    count_processed = 0
    lines_to_process = batch_process_file_line_by_line(file_path, 10)
    total = count_number_of_items_in_multidimensional_list(lines_to_process)
    page_index = 0
    for page in lines_to_process:
        if page_index == 5:
            i = 0
            for query in page:
                i += 1
                if i > 0:
                    results = SearchEngine.search(query)
                    print(results)
                    res = {query: results}
                    open_json_file_and_append_json(output_absolute_file_path, res)
                    count_processed += 1
                    print(f"Processed {count_processed} out of {total} queries")
        page_index += 1


if __name__ == '__main__':
    run()
