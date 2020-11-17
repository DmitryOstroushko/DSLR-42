"""
Functions for working with data in log reg project
"""

from typing import List, Tuple
import numpy as np  # type: ignore


def preprocessing(dataset: np.array) -> Tuple[List[str], List[str], np.array]:
    """
    The function processes data: splits dataset on 3 parts
    Returns sorted list of names of houses, list of names of features,
    values of features
    """
    data = np.delete(dataset, 0, axis=1)
    data = np.delete(data, [1, 2, 3, 4], axis=1)
    features = list(data[0])
    data = data[1:, :]
    houses = list(dict.fromkeys(data[:, 0]))
    return sorted(houses), features, data


def get_house_data(data: np.array, houses: List[str]) -> List[np.array]:
    """
    The function splits data between houses and results array of values of features for each house
    Length of returning array is equal length of houses array
    """
    data_house: List[np.array] = []
    for idx_house, _ in enumerate(houses):
        data_house.append(data[data[:, 0] == houses[idx_house]])
    return data_house


def get_one_pair_house_data(data_house: List[np.array],
                            houses: List[str],
                            idx_house_1: int,
                            idx_house_2: int) -> Tuple[List[np.array], List[np.array]]:
    """
    The function returns data for one pair of houses
    """
    data_house_1: List[np.array] = []
    data_house_2: List[np.array] = []
    for idx, _ in enumerate(houses):
        data_house_1.append(np.array(data_house[idx][:, idx_house_1], dtype=float))
        data_house_2.append(np.array(data_house[idx][:, idx_house_2], dtype=float))
    return data_house_1, data_house_2
