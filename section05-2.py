# Section05-2
# BeautifulSoup
# BeautifulSoup 사용 스크래핑(2) - 이미지 다운로드 

import os 
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Header 정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [('User-agent', UserAgent().ie)]
# Header 정보 삽입 
req.install_opener(opener)

# 브랜디 이미지 기본 URL(크롬 개발자 도구)
base = 'https://sonyunara.com/shop/search.php?searchOrder=&keyword='
# 검색어 
quote = rep.quote_plus('티셔츠')
# URL 완성 
url = base + quote 
# 요청 URL 확인 
print('Request URL : {}'.format(url))

# Request
res = req.urlopen(url)

# 이미지 저장 경로 
savePath = '/Users/sdk/imagedown/'

# 폴더 생성 예외 처리(문제발생시 프로그램 종료)
try:
    if not (os.path.isdir(savePath)):
        # 없으면 폴더 생성 
        os.makedirs(os.path.join(savePath))
except OSError as e:
    # 에러내용
    print('folder creation failed.')
    print('folder name : {}'.format(e.filename))

    # 런타임 에러 
    raise RuntimeError('System Exit')
else:
    # 폴더 생성이 되었거나, 존재할 경우 
    print('folder is created!') 

# bs4 초기화 
soup = BeautifulSoup(res, 'html.parser')
#print(soup.prettify())
print('**************')
# select 사용
img_list = soup.select('ul.item > li > div > a >img') 
print(img_list)

for i, img in enumerate(img_list,1):
    print()
    print()
    # 속성 확인
    #print(img['src'], i)
    # 저장 파일명 및 경로 
    fullfileName = os.path.join(savePath, savePath+str(i)+'.png')
    # 파일명 
    #print(fullfileName)
    # 다운로드 요청(URL, 다운로드 경로)
    req.urlretrieve(img['src'], fullfileName)

print('download succeeded!')
