# selenium 사용 실습(2)

# selenium 임포트
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")

# webdriver 설정(chrome, Firefox등 - Headless모드)
browser = webdriver.Chrome('./bin/chromedriver', options=chrome_options)

# webdriver 설정(chrome, Firefox등 - 일반모드)
#browser = webdriver.Chrome('./bin/chromedriver')

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

time.sleep(2)

# bs4 초기화 
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 소스코드 정리 
#print(soup.prettify())
pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

# 상품 리스트 확인 
#print(pro_list)

# 필요 정보 출력 
for v in pro_list:
    # 임시 출력 
    # print(v)
    if not v.find('div', class_='ad_header'):
        # 상품명, 이미지, 가격
        print()
        print(v.select('p.prod_name > a')[0].text.strip())
        a = v.select('img.image_lazy')
        for i in a:
            print('http:'+i['data-original'])

        print(v.select('p.price_sect > a > strong')[0].text)

  