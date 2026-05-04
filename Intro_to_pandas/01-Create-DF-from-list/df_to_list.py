import pandas as pd

data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

def create_dataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=["student ID", "age"])
    return df
