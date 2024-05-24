import pandas as pd

# https://velog.io/@euisuk-chung/파이썬-시각화-마스터하기-Pandas

# Pandas 데이터 객체

################################################
# 1. 리스트를 사용하여 DataFrame 객체 생성하기
data = [['A', 1], ['B', 2], ['C', 3]]
df = pd.DataFrame(data, columns=['col1', 'col2'])
#   col1  col2
# 0    A     1
# 1    B     2
# 2    C     3

################################################
# 2. 딕셔너리를 사용하여 DataFrame 객체 생성하기
data = {'col1': ['A', 'B', 'C'], 'col2': [1, 2, 3]}
df = pd.DataFrame(data)
#   col1  col2
# 0    A     1
# 1    B     2
# 2    C     3

# 3. CSV 파일을 사용하여 DataFrame 객체 생성하기
df = pd.read_csv('data.csv')

################################################
# 4. 선택하기
# 4.1 열 선택하기
col1 = df['col1']
# 0    A
# 1    B
# 2    C

col12 = df[['col1', 'col2']]
# Name: col1, dtype: object
#   col1  col2
# 0    A     1
# 1    B     2
# 2    C     3

# 4.2 행 선택하기
row0 = df.loc[0]
# col1    A
# col2    1

row012 = df.loc[[0, 1, 2]]
# Name: 0, dtype: object   col1  col2
# 0    A     1
# 1    B     2
# 2    C     3

################################################
# 5. 조작하기

# 열 추가하기
df['col3'] = [4, 5, 6]
#   col1  col2  col3
# 0    A     1     4
# 1    B     2     5
# 2    C     3     6

# 열 삭제하기
df.drop('col3', axis=1, inplace=True)
#   col1  col2
# 0    A     1
# 1    B     2
# 2    C     3

# 행 추가하기
df.loc[3] = ['D', 4]
#   col1  col2
# 0    A     1
# 1    B     2
# 2    C     3
# 3    D     4

# # 행 삭제하기
df.drop(3, inplace=True)
#   col1  col2
# 0    A     1
# 1    B     2
# 2    C     3

# 열 이름 변경하기
df.rename(columns={'col1': 'new_col1'}, inplace=True)
#   new_col1  col2
# 0        A     1
# 1        B     2
# 2        C     3

################################################
# 6. Series 객체
# Series 객체는 인덱스와 값으로 이루어진 1차원 데이터를 다루기 위한 객체입니다.
# Series 객체는 DataFrame 객체에서 열을 선택하여 추출할 수 있습니다.
data = [1, 2, 3]
s = pd.Series(data, index=['a', 'b', 'c'])
# a    1
# b    2
# c    3
# dtype: int64

# 딕셔너리를 사용하여 Series 객체 생성하기
data = {'a': 1, 'b': 2, 'c': 3}
s = pd.Series(data)
# a    1
# b    2
# c    3
# dtype: int64

################################################
