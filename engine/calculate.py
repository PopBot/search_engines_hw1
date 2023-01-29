from urllib import parse
from engine.scraping import parse_base_url_path_parameters_query_more
from engine.input_output import get_absolute_file_path_for_relative_file
import json


def convert_nested_dict_to_list(nested_dict: dict) -> list:
    # Given nested dictionary, read in order from top down the keys, then add to a list where
    # the first element is the key, and the second element is the value
    # nested_dict is a dictionary
    # returns a list
    list_of_lists = []
    for key, value in nested_dict.items():
        list_of_lists.append([key, value])
    return list_of_lists


def fix_all_root_urls(root_urls: list[str]) -> list[str]:
    # Given a list of root URLs, returns a list of fixed root URLs
    # root_urls is a list of strings
    # returns a list of strings
    fixed_root_urls = []
    for root_url in root_urls:
        fixed_root_urls.append(parse_base_url_path_parameters_query_more(root_url))
    return fixed_root_urls


def calculate_difference(x, y):
    return x - y


def calculate_d_squared(difference):
    return difference ** 2


def calculate_denominator(count: int):
    return count * (count ** 2 - 1)


def generate_diff(x: list[str], y: list[str]) -> list[int]:
    # Given two lists of strings, compare the indices of matching strings from x to y
    # and return a list of the differences in indices. Only use matching strings.
    # x and y are lists of strings
    # returns a list of integers
    diff = []

    for i in range(len(x)):
        if x[i] in y:
            diff.append(y.index(x[i]) - i)
    return diff


def get_results(google_results: list[str], yahoo_results: list[str]):
    # Given two lists of strings, compare the indices of matching strings from x to y
    google = fix_all_root_urls(google_results)
    yahoo = fix_all_root_urls(yahoo_results)
    diff = generate_diff(google, yahoo)
    spearman_coefficient = 0
    percent_overlap = 0
    if len(diff) > 1:
        squared_diffs = [d ** 2 for d in diff]
        sum_squared_diffs = sum(squared_diffs)
        numerator = 6 * sum_squared_diffs
        denominator = calculate_denominator(len(diff))
        percent_overlap = 100 * (len(diff) / len(google_results))  # Number of matching results / Number of results from Google
        spearman_coefficient = 1 - (numerator / denominator)
    elif len(diff) == 1:    # Just one matching result
        spearman_coefficient = 1
        percent_overlap = 100 * (len(diff) / len(google_results))  # Number of matching results / Number of results from Google

    return len(diff), percent_overlap, spearman_coefficient


def process_queries():
    index = 0
    average_percentage_data = []
    average_coefficient_data = []
    average_count_matches_data = []
    results_to_write = ['Queries, Number of Overlapping Results, Percent Overlap, Spearman Coefficient']
    yahoo_results = get_absolute_file_path_for_relative_file("results.json")
    google_results = get_absolute_file_path_for_relative_file("Google_Result2.json")
    # Read the results from the files
    yahoo_results_data = json.load(open(yahoo_results))
    google_results_data = json.load(open(google_results))
    for query in google_results_data.keys():
        index += 1
        google_data = google_results_data[query]
        yahoo_data = yahoo_results_data[query]
        count_matches, percent_overlap, spearman_coefficient = get_results(google_data, yahoo_data)
        average_percentage_data.append(percent_overlap)
        average_count_matches_data.append(count_matches)
        average_coefficient_data.append(spearman_coefficient)
        results_to_write.append(f"Query {index}, {count_matches}, {percent_overlap}, {spearman_coefficient}")
    average_percentage = sum(average_percentage_data) / len(average_percentage_data)
    average_count_matches = sum(average_count_matches_data) / len(average_count_matches_data)
    average_coefficient = sum(average_coefficient_data) / len(average_coefficient_data)
    results_to_write.append(f"Averages, {average_count_matches}, {average_percentage}, {average_coefficient}")
    with open(get_absolute_file_path_for_relative_file("hw1.csv"), "w") as f:
        f.write("\n".join(results_to_write))


def write_results_out_to_file():
    yahoo_results = get_absolute_file_path_for_relative_file("results.json")
    pass
