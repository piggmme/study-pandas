## Python String
https://www.pythontutorial.net/python-basics/python-string/

### 파이썬에서 문자열을 표현하는 방법
1. `'hello world!'`

2. `"hello world!"`

3. `'It\'s also a valid string'`

=> '' 문자열 에서 ' 을 사용하고 싶은경우 \ 를 앞에 붙여줌

4. `r'C:\python\bin'`

=> 파이선 인터프리터는 "\\\`" 를 특별하게 해석하는데, 그걸 방지하고 싶다면 문자열 앞에 "r`" 를 붙여주면 됨

5. 줄바꿈이 있는 문자열은 `'''...'''` , `"""..."""`

```python
help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''
```

###  변수가 들어간 문자열은 f-strings

```python
name = 'John'
message = f'Hi {name}'
print(message) # Hi John
```

###  문자열 연결하기
그냥 문자열을 나열해서 작성하면 하나의 문자열로 합쳐줌.
```python
greeting = 'Good ' 'Morning!'
print(greeting) # Good Morning!
```

###  변수에 담긴 문자열은 + 연산자로 연결
```python
greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting) # Good Afternoon!
```


###  문자열 요소에 접근하기
```python
str = "Python String"
```

1. str[0] => P
2. str[-1] => g

```
+---+---+---+---+---+---+---+---+---+---+---+---+---+
| P | y | t | h | o | n |   | S | t | r | i | n | g | 
+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9   10  11  12
-13  -12  -11  -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 
```

###  문자열 길이
`len(str)`

###  문자열 자르기
`string[start:end]`

```python
str = "Python String"
print(str[0:2]) # Py
```

### 문자열은 불변
```python
str = "Python String"
str[0] = 'J' # Error!!
```