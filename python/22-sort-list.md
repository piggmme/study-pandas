## Python Sort List

https://www.pythontutorial.net/python-basics/python-sort-list/

- 파이썬 리스트 sort()  메서드를 사용하여 원본 list 를 수정하여 정렬합니다. 
- sort()  메서드는 문자열 요소를 알파벳 순서로 정렬하고 숫자 요소는 가장 작은 것부터 가장 큰 것까지 정렬합니다.
- 기본 정렬 순서를 반대로 하려면 sort(reverse=True) 를 사용합니다.
- 복잡한 리스트에서 정렬을 위해 key 함수를 전달하여 어떤 조건을 기준으로 정렬할지 지정할 수 있다.

```python
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

# sort the companies by revenue
companies.sort(key=lambda company: company[2])

# show the sorted companies
print(companies)
```
