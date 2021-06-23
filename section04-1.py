# Section04-1 
# Requests 
# request 사용 스크래핑(1) - Session

import requests

# # 세션 활성화 
# s = requests.Session()
# r = s.get('https://www.naver.com')

# # 수신 데이터 
# # print(r.text)

# # 수신 상태 코드 
# print('Status Code : {}'.format(r.status_code))

# # 확인 
# print('OK : {}'.format(r.ok))

# # 세션 비활성화 
# s.close()

# 쿠키 Return 

s = requests.Session()
r1 = s.get('https://httpbin.org/cookies', cookies={'name': 'kim'})
print(r1.text)

# 쿠키 Set 
r2 = s.get('https://httpbin.org/cookies/set', cookies={'name': 'kim2'})
print(r2.text)

# User-Agent
url = 'https://httpbin.org'
headers = {'user-agent': 'nice-man_1.0.0_win10_ram16_home_chrome'}

# Header 정보 전송 
r3 = s.get(url, headers=headers)
print(r3.text)

# 세션 비활성화 
s.close()

# with문 사용(권장) -> 파일,DB, HTTP
with requests.Session() as s:
    r = s.get('https://daum.net')
    print(r.text)
    print(r.ok)


