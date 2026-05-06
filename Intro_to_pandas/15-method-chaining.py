"""
Write a solution to list the names of animals that strictly weigh more than 100 kilograms.

Return the animal name sorted by weight in descending order.
"""

import pandas as pd

def find_heavy_animals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals.weight > 100].sort_values(by='weight', ascending=False)[['name']]

