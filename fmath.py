"""
Functions for calculating on array items
"""
import numpy as np  # type: ignore


def count_(data: np.array) -> int:
    """
    To count quantity of items in array
    """
    try:
        data = data[~np.isnan(data)]
        data = data.astype('float64')
        return len(data)
    except TypeError:
        return len(data)


def mean_(data: np.array) -> np.float64:
    """
    To count mean value of items in array
    """
    total = 0.0
    for item in data:
        if np.isnan(item):
            continue
        total = total + item
    return total / len(data)


def std_(data: np.array) -> np.float64:
    """
    To count standard deviation value of items in array
    """
    mean = mean_(data)
    total = 0.0
    for item in data:
        if np.isnan(item):
            continue
        total = total + (item - mean) ** 2
    return (total / len(data)) ** 0.5


def min_(data: np.array) -> np.float64:
    """
    To define min item in array
    """
    min_value = data[0]
    for item in data:
        val = item
        if val < min_value:
            min_value = val
    return min_value


def max_(data: np.array) -> np.float64:
    """
    To define max item in array
    """
    min_value = data[0]
    for item in data:
        val = item
        if val > min_value:
            min_value = val
    return min_value


def percentile_25_(data: np.array) -> np.float64:
    """
    To calculate percentile 25%
    """
    return percentile_(data, 25)


def percentile_50_(data: np.array) -> np.float64:
    """
    To calculate percentile 50%
    """
    return percentile_(data, 50.0)


def percentile_75_(data: np.array) -> np.float64:
    """
    To calculate percentile 75%
    """
    return percentile_(data, 75.0)


def percentile_(data: np.array, percentage: np.float64) -> np.float64:
    """
    To calculate percentile
    """
    data.sort()
    split_point = int(round(len(data) * percentage / 100 + 0.5))
    return data[split_point - 1]


def percentile_var1_(data: np.array, percentage: np.float64) -> np.float64:
    """
    To calculate percentile
    """
    data.sort()
    split_point = len(data) * percentage / 100
    split_point_ceil = np.ceil(split_point)
    return data[int(split_point_ceil) - 1]


def percentile_var2_(data: np.array, percentage: np.float64) -> np.float64:
    """
    To calculate percentile: variant 2
    """
    data.sort()
    split_point = (len(data) - 1) * (percentage / 100)
    split_point_floor = np.floor(split_point)
    split_point_ceil = np.ceil(split_point)

    if split_point_floor == split_point_ceil:
        return data[int(split_point)]

    term_0 = data[int(split_point_floor)] * (split_point_ceil - split_point)
    term_1 = data[int(split_point_ceil)] * (split_point - split_point_floor)

    return term_0 + term_1
