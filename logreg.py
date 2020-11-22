"""
The module contains MyLogisticRegressionClass (the model) with methods.
The object of the class is initialized by parameters: a thetas array, an alpha step and
quantity of iterations for gradient descent.
The object of the is in fact the model of logistic regression which uses sigmoid function
to calculate an error on the each step and to move on gradient.
"""

from typing import Tuple, List
from tqdm import tqdm  # type: ignore
import numpy as np  # type: ignore
from fmath import mean_, std_


class MyLogisticRegressionClass:
    """
    The class with methods of the logistic regression model

    Attributes:
        thetas: an array of coefficient of a regression
        alpha: an alpha step
        n_iter: quantity of iterations
    """
    def __init__(self, thetas: List = None, alpha: np.float64 = 5e-5, n_iter: int = 30000) -> None:
        """
        Initializes object of MyLogisticRegressionClass with initial values
        """
        self.alpha = alpha
        self.n_iter = n_iter
        self.thetas = [] if thetas is None else thetas

    def fit(self, dataset: List[np.array], features: List[str]) -> List:
        """
        The method calculates and returns an array of thetas values,
        i.e learns of model.

        Args:
            dataset: a list of rows with data - a data set
            features: a list of names of features

        Returns:
            A thetas array
        """
        data_x, data_y = self.processing(dataset, features)
        data_x = np.insert(data_x, 0, 1, axis=1)
        for house in np.unique(data_y):
            print('Model training for house ', house)
            y_copy = np.where(data_y == house, 1, 0)
            thetas: List[np.float64] = np.ones(np.array(data_x).shape[1])

            for _ in tqdm(range(self.n_iter)):
                output = np.array(np.array(data_x).dot(thetas), dtype=np.float64)
                errors = np.array(y_copy - self._sigmoid(output), dtype=np.float64)
                gradient = np.array(np.dot(np.array(data_x).T, errors), dtype=np.float64)
                thetas += self.alpha * gradient
            self.thetas.append((thetas, house))
        return self.thetas

    def processing(self, dataset: List[np.array], features: List[str], drop_nan: bool = True) -> \
            Tuple[np.array, np.array]:
        """
        The function gets data set: columns are features, target, other columns
        Processing:
        - to save target and features columns (deletes other columns)
        - to delete rows with NULL value at least in one column

        Args:
            dataset: a data set
            features: a list of names of features
            drop_nan: a boolean key, if True the program drops rows with nan values from
            the data set

        Returns:
            values of features (n columns)
            target column
        """
        res_dataset = self._drop_nan(dataset, len(features)) if drop_nan else dataset
        ds_features = np.array(res_dataset)[:, 1:]
        ds_target = np.array(res_dataset)[:, 0]
        np.apply_along_axis(self._scaling, 0, ds_features)
        return ds_features, ds_target

    @staticmethod
    def _drop_nan(dataset: List[np.array], q_features: int) -> List[np.array]:
        """
        Static method drops rows with nan values and returns new data set

        Args:
            dataset: a data set
            q_features: quantity of features

        Returns:
            A data set without rows which contains nan values
        """
        res_dataset: List[np.array] = []
        for line_data in dataset:
            values = np.array(line_data[1:], dtype=np.float64)
            if len(values[~np.isnan(values)]) + 1 != q_features:
                continue
            res_dataset.append(line_data)
        return np.array(res_dataset, dtype=object)

    @staticmethod
    def _scaling(data: List[np.array]) -> List[np.array]:
        """
        Static method for scaling of data:
        - to subtract mean of data
        - to divide by the standard deviation

        Args:
            data: a data set

        Returns:
            a scaling data set
        """
        mean_data = mean_(data)
        std_data = std_(data)
        for line in enumerate(data):
            data[line[0]] = (data[line[0]] - mean_data)/std_data
        return data

    @staticmethod
    def _sigmoid(data: np.array) -> np.array:
        """
        Static method to calculate SIGMOID function (logistic function) for fata
        The result of the method is uses to calculate error.

        Args:
            data: a data set

        Returns:
            a data set as a result of sigmoid function to calculate error
        """
        return 1 / (1 + np.exp(-data))

    def _predict_one(self, data_x: np.array) -> np.float64:
        """
        The method calculates for single data row probabilities to be marks of class
        After than returns prediction for CLASS: with max value

        Args:
            data_x: single data row

        Returns:
            a probability for the input data row
        """
        return max((data_x.dot(w), c) for w, c in self.thetas)[1]

    def predict(self, data_x: List[np.array]) -> List[np.array]:
        """
        The method predicts marks the CLASS for the entire data set

        Args:
            data_x: a data set

        Returns:
            List of predictions
        """
        return [self._predict_one(item) for item in np.insert(data_x, 0, 1, axis=1)]

    def score(self, dataset: List[np.array], features: List[str]) -> np.float64:
        """
        The method calculates score: accuracy of the model

        Args:
            dataset: a data set
            features: a list of names of features

        Returns:
            Accuracy score
        """
        data_x, data_y = self.processing(dataset, features)
        return sum(self.predict(data_x) == data_y) / len(data_y)
