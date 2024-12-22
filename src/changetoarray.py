import numpy as np
import typing
from numpy.typing import NDArray
import pandas as pd

def change_array_x(dataframe: pd.DataFrame) -> NDArray[np.float_]: 
    """
    Converts the first column of a DataFrame to a NumPy array.
    
    Parameters:
        dataframe (pd.DataFrame): Input DataFrame with at least one column.

    Returns:
        NDArray[np.float_]: NumPy array containing values of the first column.
    """
    arr_df_x = np.array(dataframe[dataframe.columns[0]])
    return arr_df_x  

def change_array_y(dataframe: pd.DataFrame) -> NDArray[np.float_]:
    """
    Converts the second column of a DataFrame to a NumPy array.
    
    Parameters:
        dataframe (pd.DataFrame): Input DataFrame with at least two columns.

    Returns:
        NDArray[np.float_]: NumPy array containing values of the second column.
    """
    arr_df_y = np.array(dataframe[dataframe.columns[1]])
    return arr_df_y

    