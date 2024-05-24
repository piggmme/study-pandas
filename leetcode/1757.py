import pandas as pd

# https://leetcode.com/problems/recyclable-and-low-fat-products/description/
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filtered_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return filtered_products['product_id'].to_frame()