import pandas as pd

# https://velog.io/@euisuk-chung/파이썬-시각화-마스터하기-Pandas

# Pandas 기본 사용법

################################################
# 1. 데이터 불러오기

# 1.1 CSV 파일 불러오기
# CSV(Comma-Separated Values) 파일은 쉼표로 구분된 데이터를 저장하는 파일 형식입니다.
# 판다스에서는 read_csv() 함수를 이용하여 CSV 파일을 불러올 수 있습니다.
df = pd.read_csv('data.csv')

# 1.2 Excel 파일 불러오기
# Excel 파일은 스프레드시트 프로그램에서 생성한 데이터를 저장하는 파일 형식입니다.
# 판다스에서는 read_excel() 함수를 이용하여 Excel 파일을 불러올 수 있습니다.
df = pd.read_excel('data.xlsx')

################################################
# 2. 데이터 살펴보기

# 2.1 데이터프레임 정보 확인하기
# info() 함수는 데이터프레임의 정보를 출력합니다.
# 데이터프레임의 크기, 데이터 타입, 결측치 등의 정보를 확인할 수 있습니다.
df.info()

# 2.2 데이터프레임 일부 데이터 보기
# head() 함수는 데이터프레임의 첫 n행을 출력합니다.
# n은 인자로 전달될 수 있습니다. 기본값은 5입니다.
df.head()

# 데이터프레임 요약 통계량 보기
# describe() 함수는 데이터프레임의 요약 통계량을 출력합니다.
# 각 열의 개수, 평균, 표준편차, 최소값, 25% 백분위수, 중앙값, 75% 백분위수, 최대값 등의 정보를 확인할 수 있습니다.
df.describe()

################################################
# 3. 데이터 선택하기

data = [['A', 1], ['B', 2], ['C', 3]]
df = pd.DataFrame(data, columns=['col1', 'col2'])

# 3.1 열 선택하기
# 열 이름을 사용하여 데이터프레임의 열을 선택할 수 있습니다.
# df['열 이름']
col1 = df['col1']

# 0    A
# 1    B
# 2    C

# 여러 개의 열을 선택할 때는 리스트 형태로 열 이름을 전달합니다.
# df[['열 이름 1', '열 이름 2', ...]]
col12 = df[['col1', 'col2']]

# Name: col1, dtype: object
#   col1  col2
# 0    A     1
# 1    B     2
# 2    C     3

# 3.2 행 선택하기
# 특정한 행을 선택할 때는 loc[] 함수를 사용합니다.
# loc[] 함수는 행의 이름 또는 인덱스를 사용하여 행을 선택합니다.
# df.loc[행 이름 또는 인덱스]
row0 = df.loc[0]

# col1    A
# col2    1

# 여러 개의 행을 선택할 때는 리스트 형태로 행 이름 또는 인덱스를 전달합니다.
# df.loc[[행 이름 1, 행 이름 2, ...]]
row012 = df.loc[[0, 1, 2]]

# Name: 0, dtype: object
#   col1  col2
# 0    A     1
# 1    B     2
# 2    C     3

################################################
# 4. 데이터 필터링하기

# 4.1 조건 필터링
# 조건 필터링은 [] 연산자와 조건식을 이용하여 수행합니다.

# df[조건식]

# 2010년 이후의 데이터만 선택하기
df[df['Year'] >= 2010]

# 4.2 논리 연산자 사용하기
# &(and)와 |(or) 연산자를 이용하여 논리 연산을 수행할 수 있습니다.

# df[(조건식 1) & (조건식 2)]
# df[(조건식 1) | (조건식 2)]

# 2010년 이후이면서 금메달 이상을 획득한 데이터만 선택하기
df[(df['Year'] >= 2010) & (df['Medal'] == 'Gold')]

# 4.3 isin() 함수 이용하기
# isin() 함수를 이용하여 특정한 값이 포함된 데이터만 선택할 수 있습니다.

# df[df['열 이름'].isin([값1, 값2, ...])]

# 'KOR', 'USA', 'JPN' 국가의 데이터만 선택하기
df[df['NOC'].isin(['KOR', 'USA', 'JPN'])]

################################################
# 5. 데이터 그룹화하기
# 데이터프레임에서는 특정한 기준에 따라 데이터를 그룹화하여 처리할 수 있습니다.

# 5.1. groupby() 함수 이용하기
# groupby() 함수를 이용하여 특정한 열을 기준으로 데이터를 그룹화할 수 있습니다.

# df.groupby('열 이름')
# groupby() 함수로 그룹화한 데이터는 각 그룹에 대한 정보를 담고 있는 객체입니다.
# 이를 바탕으로 다양한 처리를 수행할 수 있습니다.


# 5.2. 집계 함수 이용하기
# 그룹화된 데이터에 대해 집계 함수를 이용하여 다양한 처리를 수행할 수 있습니다.
# 그룹화된 데이터.집계함수()

# count() : 데이터의 개수를 세는 함수
# sum() : 데이터의 합을 구하는 함수
# mean() : 데이터의 평균을 구하는 함수
# median() : 데이터의 중앙값을 구하는 함수
# min() : 데이터의 최소값을 구하는 함수
# max() : 데이터의 최대값을 구하는 함수
# std() : 데이터의 표준편차를 구하는 함수
# var() : 데이터의 분산을 구하는 함수

df.groupby('col').count()
df.groupby('col').sum()
df.groupby('col').mean()
df.groupby('col').median()
df.groupby('col').min()
df.groupby('col').max()
df.groupby('col').std()
df.groupby('col').var()

# 예를 들어, 국가별 금메달 수의 합계를 구하고 싶을 때는 다음과 같이 작성할 수 있습니다.
# 국가별 금메달 수의 합계 구하기
df[df['Medal'] == 'Gold'].groupby('NOC')['Medal'].count()

################################################
# 6. 데이터 정렬하기
# 데이터프레임에서는 특정한 열을 기준으로 데이터를 정렬할 수 있습니다.
# 기본적으로 오름차순으로 정렬되며, 내림차순으로 정렬하려면 ascending=False 옵션을 추가합니다.

# 오름차순으로 정렬하기
df.sort_values('열 이름')

# 내림차순으로 정렬하기
df.sort_values('열 이름', ascending=False)

# 예를 들어, 아래와 같은 데이터프레임이 있다고 가정해 봅시다.
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 32, 18, 47],
    'city': ['New York', 'Paris', 'London', 'San Francisco']
    }
df = pd.DataFrame(data)
#       name  age           city
# 0    Alice   25       New York
# 1      Bob   32          Paris
# 2  Charlie   18         London
# 3    David   47  San Francisco

df.sort_values('age')
#       name  age           city
# 0    Alice   25       New York
# 1      Bob   32          Paris
# 2  Charlie   18         London
# 3    David   47  San Francisco

################################################
# 7. 인덱스 초기화하기

# 데이터프레임에서는 reset_index() 함수를 이용하여 인덱스를 초기화할 수 있습니다.
# 이때 기존 인덱스는 열로 추가됩니다.
df.reset_index()

# 예를 들어, 아래와 같은 데이터프레임이 있다고 가정해 봅시다.
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 32, 18, 47],
    'city': ['New York', 'Paris', 'London', 'San Francisco']
    }
df = pd.DataFrame(data)
df.set_index('name', inplace=True)
#          age           city
# name
# Alice     25       New York
# Bob       32          Paris
# Charlie   18         London
# David     47  San Francisco

# 이제 인덱스를 초기화해 보겠습니다.
df.reset_index()
#       name  age           city
# 0    Alice   25       New York
# 1      Bob   32          Paris
# 2  Charlie   18         London
# 3    David   47  San Francisco
################################################
