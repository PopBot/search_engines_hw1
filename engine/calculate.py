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





#############

import time


def spearmans_rank_correlation_coefficient(x, y):
    # x and y are lists of numbers of the same length
    # returns the Spearman's rank correlation coefficient
    # between x and y
    # https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient
    x_rank = rank(x)
    y_rank = rank(y)
    return pearsons_correlation_coefficient(x_rank, y_rank)


def rank(x):
    # x is a list of numbers
    # returns a list of ranks of the numbers in x
    # https://en.wikipedia.org/wiki/Ranking
    sorted_x = sorted(x)
    rank = []
    for i in range(len(x)):
        rank.append(sorted_x.index(x[i]) + 1)
    return rank


def pearsons_correlation_coefficient(x, y):
    # x and y are lists of numbers of the same length
    # returns the Pearson's correlation coefficient
    # between x and y
    # https://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum([i ** 2 for i in x])
    sum_y_squared = sum([i ** 2 for i in y])
    psum = sum([x[i] * y[i] for i in range(n)])
    num = psum - (sum_x * sum_y / n)
    den = ((sum_x_squared - sum_x ** 2 / n) * (sum_y_squared - sum_y ** 2 / n)) ** .5
    if den == 0:
        return 0
    return num / den


def calculate_spearman_rank_coefficient():
    pass







YAHOO_SEARCH_URL = "https://search.yahoo.com/search?p="