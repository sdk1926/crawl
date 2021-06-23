# section02-3 
# lxml 사용 기초 스크래핑(1)
# pip install lxml, requests, cssselect

import requests 
import lxml.html
import cssselect
def main():
    """
    네이버 메인 뉴스 스탠드 스크래핑 함수 
    """
    # 스크래핑 대상 URL
    response = requests.get("https://www.naver.com")

    # 신문사 링크 리스트 획득 
    urls = scrape_news_list_page(response)

    # 결과 출력 
    for url in urls:
        # url 출력 
        print(url)
        # 파일 쓰기
        # 생략 

def scrape_news_list_page(response):
    # url 리스트 선언 
    urls = []

    # 태그 정보 문자열 저장 
    # print(response.content)
    root = lxml.html.fromstring(response.content)
    
    for a in root.cssselect('.thumb_area .thumb_box .popup_wrap a.btn_popup'):

        url = a.get('href')
        if '#' not in url:
            urls.append(url)
    
    return urls


# 스크래핑 시작 
if __name__ == "__main__":
    main()
