# section 03-2 
# Get 방식 데이토통신(2) - RSS

import urllib.request 
import urllib.parse 

# 행정 안전부 : https://www.mois.go.kr 
# 행정 안전부 RSS API URL 
API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001,1012,1013, 1014]:
    params.append(dict(ctxCd=num))

# 중간 확인 
# print(params)

# 연속해서 4회 요청 
for c in params:
    # 파라미터 출력 
    # print(c)
    # url 인코딩 
    param = urllib.parse.urlencode(c)

    # url 완성 
    url = API + '?' + param
    # URL 출력 
    print("url : ", url)

    # 요청 
    res_data = urllib.request.urlopen(url).read()
    #print(res_data)
    # 수신 후 디코딩 
    contents = res_data.decode('UTF-8')
    
    # 출력 
    print('*' * 100)
    print(contents)


