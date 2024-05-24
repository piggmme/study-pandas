## Python Functions

https://www.pythontutorial.net/python-basics/python-functions/

- 파이썬 함수는 작업을 수행하거나 값을 반환하는 재사용 가능한 명명된 코드 블록입니다.
- 새 함수를 정의하려면 def  키워드를 사용합니다. 함수는 함수 정의와 본문으로 구성됩니다.
- 함수는 0개 이상의 매개변수를 가질 수 있습니다. 함수에 하나 이상의 매개변수가 있는 경우 같은 수의 인수를 전달해야 합니다.
- 함수는 작업을 수행하거나 값을 반환할 수 있습니다. 함수에서 값을 반환하려면 return 문을 사용합니다.

```python
def sum(a, b):
    return a + b


total = sum(10,20)
print(total)
```