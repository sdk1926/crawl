from urllib import response
import urllib.request as req 
from urllib.error import URLError, HTTPError




# 다운로드 경로 및 파일명

path_list = ['/Users/sdk/test.jpg','/Users/sdk/test.html']

# 다운로드 리소스 ㅕ기

target_url = ['https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAxMDlfMjk1%2FMDAxNjEwMTk1OTY0MTYx.7X1cq-bI_5ghfbrsqlBPytmw18WNOfrhNdO0Pk7A0Mgg.3ZIEoc9SpcLCaHpITRBnSc9XkPsKZzklP8dokbaQxtog.JPEG.erasw0715%2FNate%25A3%25DF20210109%25A3%25DF205332.jpg&type=sc960_832', "http://google.com"]

for i, url in enumerate(target_url):
    # 예외 처리 
    try:
        # 웹 수신 정보 읽기 
        response = req.urlopen(url)

        # 수신 내용 
        contents = response.read()

        print('--------------------------')

        # 상태 정보 중간 출력 
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print('------------')

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print('Download failed')
        print('HTTPError Code : ', e.code)
    except URLError as e:
        print('Download failed')
        print("URL Error Reason : ", e.reason)

    # 성공 
    else:
        print()
        print("Download Succeed.")