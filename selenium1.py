# selenium 사용 실습(1) - 설정 및 기본 테스트 


from selenium import webdriver

# webdriver 설정(chrome)
browser = webdriver.Chrome('./bin/chromedriver')

# 크롬 브라우저 내부 대기 
browser.implicitly_wait(5)

# 속성 확인 
print(dir(browser))

# 브라우저 사이즈 
browser.set_window_size(1080,720) # maxmize_window(), minimize_window()

# 페이지 이동 
browser.get('https:/www.daum.net')

# 페이지 내용 
print('Page contents : {}'.format(browser.page_source))
print()

# 세션 값 출력 
print('Session ID : {}'.format(browser.session_id))

# 타이틀 출력 
print('Title : {}'.format(browser.title))

# 현재 URL 출력
print('URL : {}'.format(browser.current_url))

# 현재 쿠키 출력 
print('Cookies : {}'.format(browser.get_cookies()))

# 검색창 인풋
element = browser.find_element_by_css_selector('div.inner_search > input#q')

# 검색어 입력 
element.send_keys('블랙핑크')

# form submit 
element.submit()

# 스크린샷 저장1
browser.save_screenshot('/Users/sdk/imagedown/bpsearch.jpg')

# 스크린샷 저장2
browser.get_screenshot_as_file('/Users/sdk/imagedown/bpsearch2.jpg')

# 브라우저 종료 
browser.quit()