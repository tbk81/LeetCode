"""
Write a solution to calculate and display the number of rows and columns of players.
Return the result as an array:
[number of rows, number of columns]
"""

import pandas as pd

def get_dataframe_size(players: pd.DataFrame) -> List[int]:
    row, col = players.shape
    return [row, col]
