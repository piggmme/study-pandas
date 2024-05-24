## Python while

https://www.pythontutorial.net/python-basics/python-while/

- 조건이 True인 경우 Python while  루프 문을 사용하여 코드 블록을 실행합니다.

예시

```python
command = ''

while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")
```

출력
```
>Hi
Echo: Hi
>Python while
Echo: Python while
>quit
Echo: quit
```