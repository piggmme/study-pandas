# https://leetcode.com/problems/article-views-i/description/

import pandas as pd

# 내 코드
# def article_views(views: pd.DataFrame) -> pd.DataFrame:
#     filtered = views[views['author_id'] == views['viewer_id']].rename(columns={'author_id': 'id'})
#     return (
#             filtered['id']
#             .sort_values()
#             .drop_duplicates()
#             .to_frame()
#            )

# 더 나은 코드
def article_views(views: pd.DataFrame) -> pd.DataFrame:

    return views[views.author_id == views.viewer_id
             ].sort_values('author_id'
             ).rename(columns = {'author_id': 'id'}
             ).drop_duplicates('id').iloc[:,[1]]