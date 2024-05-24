## Python Recursive Functions

https://www.pythontutorial.net/python-basics/python-recursive-functions/

```python
def fn():
    # ...
    if condition:
        # stop calling itself
    else:
        fn()
    # ...
```

- 재귀 함수는 호출되지 않을 때까지 스스로를 호출하는 함수입니다.
- 그리고 재귀 함수에는 항상 스스로 호출을 중지하는 조건이 있습니다.