"""
The module contains functions for calculating of the characteristics of arrays

  Typical usage examples:

  q_of_items = count_(array)
  mean_data = mean_(array)
  std_data = mean_(array)
  min_value = min_(array)
  max_value = max_(array)
  percentile25_value = percentile_25(array)
  percentile50_value = percentile_50(array)
  percentile75_value = percentile_75(array)
  percentile_value = percentile_(array, percentage)
"""

import numpy as np  # type: ignore


def count_(data: np.array) -> int:
    """
    The function counts quantity of not nan items in the array.

    Args:
        data: array

    Returns:
        Quantity of items in the array as an integer number
    """
    try:
        data = data[~np.isnan(data)]
        data = data.astype('float64')
        return len(data)
    except TypeError:
        return len(data)


def mean_(data: np.array) -> np.float64:
    """
    The function counts mean value of not nan items in the array of numbers.

    Args:
        data: array

    Returns:
        Mean value of items in the array as a float number
    """
    total = 0.0
    for item in data:
        if np.isnan(item):
            continue
        total = total + item
    return total / len(data)


def std_(data: np.array) -> np.float64:
    """
    The function counts standard deviation of not nan items in the array of numbers.

    Args:
        data: array

    Returns:
        Standard deviation of items in the array as a float number
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
    The function defines min value of not nan items in the array of numbers.

    Args:
        data: array

    Returns:
        Min value of items in the array as a float number
    """
    min_value = data[0]
    for item in data:
        val = item
        if val < min_value:
            min_value = val
    return min_value


def max_(data: np.array) -> np.float64:
    """
    The function defines max value of not nan items in the array of numbers.

    Args:
        data: array

    Returns:
        Max value of items in the array as a float number
    """
    min_value = data[0]
    for item in data:
        val = item
        if val > min_value:
            min_value = val
    return min_value


def percentile_25_(data: np.array) -> np.float64:
    """
    The function calculates percentile 25% of not nan items in the array of numbers.

    Args:
        data: array

    Returns:
        Value of percentile 25% of items in the array as a float number
    """
    return percentile_(data, 25)


def percentile_50_(data: np.array) -> np.float64:
    """
    The function calculates percentile 50% of not nan items in the array of numbers.

    Args:
        data: array

    Returns:
        Value of percentile 50% of items in the array as a float number
    """
    return percentile_(data, 50.0)


def percentile_75_(data: np.array) -> np.float64:
    """
    The function calculates percentile 75% of not nan items in the array of numbers.

    Args:
        data: array

    Returns:
        Value of percentile 75% of items in the array as a float number
    """
    return percentile_(data, 75.0)


def percentile_(data: np.array, percentage: np.float64) -> np.float64:
    """
    The function calculates percentile of not nan items in the array of numbers.

    Args:
        data: array
        percentage: float value

    Returns:
        Value of defined percentile of items in the array as a float number
    """
    data.sort()
    split_point = int(round(len(data) * percentage / 100 + 0.5))
    return data[split_point - 1]
