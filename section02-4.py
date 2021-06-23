# section02-3 
# lxml 사용 기초 스크래핑(1)
# pip install lxml, requests, cssselect

import requests 
from lxml.html import fromstring, tostring

def main():
    """
    네이버 메인 뉴스 스탠드 스크래핑 함수 
    """
    # 세션 사용 
    session = requests.Session()

    # 스크래핑 대상 URL
    response = session.get("https://www.naver.com") # Get, Post 

    # 신문사 링크 딕션너리 획득 
    urls = scrape_news_list_page(response)

    # 딕샤너리 확인
    # print(urls)

    # 결과 출력 
    for name, url in urls.items():
        # url 출력 
        
        print(name, url)
        # 파일 쓰기
        # 생략 

def scrape_news_list_page(response):
    # url 딕셔너리 선언 
    link = []
    name = []
    # 태그 정보 문자열 저장 
    # print(response.content)
    root = fromstring(response.content)
    
    #link
    for a in root.xpath('//div[@class="thumb_area"]/div/div/a'):

        link_element = a.get('href')
        if '#' not in link_element:
            link.append(link_element)
    
    for b in root.xpath('//div[@class="thumb_area"]/div/a/img'):    

        name_element = b.get('alt')
        name.append(name_element)

        # a 구조 확인 
        #print('-------bbbbb-----')
        #print(tostring(b, pretty_print=True))
   
    urls = dict(zip(name,link))
    
    return urls



# 스크래핑 시작 
if __name__ == "__main__":
    main()
