# Section04-2
# Requests
# requests 사용 스크래핑(2) - JSON

import json
import requests

s = requests.Session()

# 100개 데이터 요청 
r = s.get('https://www.httpbin.org/stream/100', stream=True)

# 수신확인 
print(r.text)

# Encoding 확인 
print('Before Encoding : {}'.format(r.encoding))

if r.encoding:
    r.encoding = 'UTF-8'

print('After Encoding : {}'.format(r.encoding))

for line in r.iter_lines(decode_unicode=True):
    # 라인 출력 후 타입 확인 
    # print(line)
    # print(type(line))
    # JSON(Dict)변환 후 타입 확인 
    b = json.loads(line) # str -> dict 
    # print(b)
    # print(type(b))    

    # 정보 내용 출력 
    for k,v in b.items():
        print('Key : {}, value : {}'.format(k,v))

    print()
    print()

s.close()

r = s.get('https://jsonplaceholder.typicode.com/todos/')

# Header 정보 
print(r.headers)

# 본문 정보 
print(r.text)

# json 변환 
print(r.json())

# key 반환 
print(r.json().keys())

# 값 반환 
print(r.json().values())

# 인코딩 반환 
print(r.encoding)

# 바이너리 정보 
print(r.content)

s.close()