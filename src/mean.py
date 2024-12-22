import numpy as np
import typing 
from numpy.typing import NDArray

def get_mean(arr_data:NDArray[np.float64])->float:
    """
    Calculate mean in a given array

    Args:
        arr_data (NDArray[np.float64]):Array of numbers

    Returns:
        float: Mean of the given array
    """
    total:float=0.0
    
    for a in arr_data:
        total+=a
        mean:float=total/len(arr_data)
    return mean

