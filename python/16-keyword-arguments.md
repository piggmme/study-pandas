#3 Python Keyword Arguments

https://www.pythontutorial.net/python-basics/python-keyword-arguments/

- 많은 인수를 허용하는 함수의 경우 함수 호출을 더 읽기 쉽고 명확하게 만들려면 파이썬 키워드 인수를 사용하세요.
- 첫 번째 키워드 인자 뒤의 모든 인자도 키워드 인자여야 합니다.

```python
def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(100, 0.1)
net_price = get_net_price(price=100, discount=0.1)
net_price = get_net_price(discount=0.1, price=100)
```