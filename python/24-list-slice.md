## Python List Slice

https://www.pythontutorial.net/python-basics/python-list-slice/

```python
sub_list = list[begin: end: step]
```

- 이 구문에서 begin, end, step 인수는 유효한 인덱스여야 합니다. 그리고 모두 선택 사항입니다.
- begin 인덱스는 기본값이 0입니다. end인덱스는 기본값이 목록 길이입니다. 그리고 step 인덱스는 기본값이 1입니다.
- 슬라이스는 begin부터 시작하여 end까지 step 스텝으로 이어집니다.
- begin, end, step계는 양수 또는 음수일 수 있습니다. 양수 값은 첫 번째 요소에서 마지막 요소로 목록을 슬라이싱하고 음수 값은 마지막 요소에서 첫 번째 요소로 목록을 슬라이싱합니다.

예시
```python
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[1:4] # ['orange', 'yellow', 'green']
```

```python
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[:3] # ['red', 'orange', 'yellow']
```

```python
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[-3:] # ['blue', 'indigo', 'violet']
```

```python
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[::2] # ['red', 'yellow', 'blue', 'violet']
```

```python

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
reversed_colors = colors[::-1]
# ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
```

```python
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors[0:2] = ['black', 'white']
# ['black', 'white', 'yellow', 'green', 'blue', 'indigo', 'violet']
```

```python
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
del colors[2:5] # ['red', 'orange', 'indigo', 'violet']
```