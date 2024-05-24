## Python Lambda Expressions

https://www.pythontutorial.net/python-basics/python-lambda-expressions/

- 파이썬 람다 표현식을 사용하여 이름이 없는 함수인 익명 함수를 만들 수 있습니다.
lambda parameters: expression

- 람다 표현식은 하나 이상의 인수를 받아들이고 표현식을 포함하며 해당 표현식의 결과를 반환합니다.

```python
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)

full_name = get_full_name(
    'John',
    'Doe',
    lambda first_name, last_name: f"{first_name} {last_name}"
)
print(full_name) # John Doe
```

- 람다 표현식을 사용하여 익명 함수를 함수에 전달하고 다른 함수에서 함수를 반환할 수 있습니다.

```python
def times(n):
    return lambda x: x * n
double = times(2)

result = double(2)
print(result) # 4
```