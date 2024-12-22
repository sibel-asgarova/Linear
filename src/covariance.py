import numpy as np
import typing
from numpy.typing import NDArray

def get_covariance(
    arr_x: NDArray[np.float64], arr_y: NDArray[np.float64], mean_x: float, mean_y: float) -> float:
    """
    Calculate the covariance between two numpy arrays.
    
    Parameters:
    arr_x (NDArray[np.float64]): Array of numbers representing variable X.
    arr_y (NDArray[np.float64]): Array of numbers representing variable Y.
    mean_x (float): Mean of arr_x.
    mean_y (float): Mean of arr_y.

    Returns:
    float: The covariance between arr_x and arr_y.
    """
    total: float = 0.0
    
    for x, y in zip(arr_x, arr_y):
        total += (x - mean_x) * (y - mean_y)
    
    covariance: float = total / len(arr_x)
    return covariance
