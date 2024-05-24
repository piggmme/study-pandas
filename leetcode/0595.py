# https://leetcode.com/problems/big-countries/description/

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    bigSeries = world[(world['area'] >= 3_000_000) | (world['population'] >= 25_000_000)]
    return bigSeries[['name', 'population', 'area']]