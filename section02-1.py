# Section 02-1
# 파이썬 크롤링 기초 
# urllib 사용법 및 기본 스크래핑

import urllib.request as req 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



# 파일 URL 
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAyMjJfMTE1%2FMDAxNjE0MDAyMTEyODc3.jR5_j5v9veu4OZOZ8ONY1rc5EDgyE_QbI8J6K22hA7Yg.IrT5FCO0bjSoC2eGGh5CAGfUrVpWJadtTgVnDsTZSUUg.JPEG.lpts505%2F%25B4%25D9%25BF%25EE%25B7%25CE%25B5%25E5.jpeg%25A3%25AD1.jpg&type=sc960_832'
html_url = 'http://google.com'

# 다운받을 경로 
save_path1 = '/Users/sdk/test.jpg'
save_path2 = '/Users/sdk/test.html'

# 예외 처리 
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download failed')
    print(e)
else: 
    # header 정보 출력 
    print(header1)
    print(header2)

    # 다운로드 파일 정보 
    print(f'Filename1 {file1}')
    print(f'Filename2 {file2}')
    print()

    # 성공
    print('Download Succeed')

