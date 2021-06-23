# selenium 사용 실습(3)

# selenium 임포트
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
# 엑셀처리 임포트
import xlsxwriter
# 이미지 바이트 처리 
from io import BytesIO
import urllib.request as req

chrome_options = Options()
chrome_options.add_argument("--headless")

# 엑셀 처리 선언
workbook = xlsxwriter.Workbook('/Users/sdk/imagedown/macbook.xlsx')

# 워크 시트
worksheet = workbook.add_worksheet()


# webdriver 설정(chrome, Firefox등 - Headless모드)
#browser = webdriver.Chrome('./bin/chromedriver', options=chrome_options)

# webdriver 설정(chrome, Firefox등 - 일반모드)
browser = webdriver.Chrome('./bin/chromedriver')

# 크롬 브라우저 내부 대기 
browser.implicitly_wait(5)

# 브라우저 사이즈 
browser.set_window_size(1080, 720) 

# 페이지 이동 
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용 
# print('Before Page Contents : {}'.format(browser.page_source))

# 제조사별 더 보기 클릭1 
# Explicitly wait

WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 제조사별 더 보기 클릭2 
# Implicitly wait 
#time.sleep(2)
#browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# 원하는 모델 카테고리 클릭 
'//*[@id="selectMaker_simple_priceCompare_A"]/li[16]/label'
WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="selectMaker_simple_priceCompare_A"]/li[16]/label'))).click()

# 2차 페이지 내용
#print('Before Page Contents : {}'.format(browser.page_source))

# 2초간 대기
time.sleep(2) 

# 현재 페이지
cur_page=1

# 크롤링 페이지 수
target_crawl_num = 6

# 엑셀 행 수
ins_cnt = 1

while cur_page <= target_crawl_num:
    # bs4 초기화 
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # 소스코드 정리 
    #print(soup.prettify())
    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

    # 상품 리스트 확인 
    #print(pro_list)

    # 페이지 번호 출력 
    print('****** current Page : {}'.format(cur_page), '******')
    print()
    # 필요 정보 출력 
    src = 'http:'
    for v in pro_list:
        # 임시 출력 
        # print(v)
        if not v.find('div', class_='ad_header'):
            # 상품명, 이미지, 가격
            product_name = v.select('p.prod_name > a')[0].text.strip()
            prod_price = v.select('p.price_sect > a > strong')[0].text
            # 엑셀 저장(텍스트)
            worksheet.write('A%s' % ins_cnt, product_name)
            worksheet.write('B%s' % ins_cnt, prod_price)
            # 이미지 요청 후 바이트 변환 
            #print(v.select('img.image_lazy')
        
            for i in v.select('img.image_lazy'):
                try:     
                    url = src+i['data-original']
                    print(url)
                    img_data = BytesIO(req.urlopen(url).read())
                    # 엑셀 저장(이미지)
                    worksheet.insert_image('C%s' % ins_cnt, product_name, {'image_data': img_data})
                except:
                    pass
                
            ins_cnt += 1
                    
            #print(v.select('p.prod_name > a')[0].text.strip())
            #print(v.select('p.price_sect > a > strong')[0].text)
        

        print()
    print()

    # 페이지 증가
    cur_page += 1

    if cur_page > target_crawl_num:
        print('Crawling Succeed')
        break

    # 페이지 이동 클릭
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()  

    # BeautifulSoup 인스턴스 삭제 
    del soup

    # 3초간 대기
    time.sleep(5)


    # 페이지 별 스크린샷 저장 
    browser.save_screenshot(f'/Users/sdk/imagedown/{cur_page}.png')
  
# 브라우저 종료 
browser.close()

# 엑셀 파일 닫기
workbook.close()

