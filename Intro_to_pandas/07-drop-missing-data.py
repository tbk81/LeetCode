"""
There are some rows that have missing values in the name column.

Write a solution to remove the rows with missing values.
"""

import pandas as pd

def drop_missing_data(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])
