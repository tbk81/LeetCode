"""
Write a solution to correct the errors:

The grade column is stored as floats, convert it to integers.
"""

import pandas as pd

def change_datatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({'grade': 'int64'})
