import numpy as np
import typing
from numpy.typing import NDArray

def get_std_x(arr_x:NDArray[np.float64],mean_x:float):
    """
    Calculate standart deviation in a given array

    Args:
        arr_x (NDArray[np.float64]):Array of numbers
        mean_x (float):Mean of given array

    Returns:
        float: Standart Deviation of the given array
    """
    total:float=0.0
    for x in arr_x:
        total+=(x-mean_x)**2
    std:float=(total/len(arr_x))**0.5
    return std