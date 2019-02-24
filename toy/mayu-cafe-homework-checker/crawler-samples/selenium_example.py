from selenium import webdriver
from bs4 import BeautifulSoup

targets = ['유인경 Iris', 'ChrisSon']
homeworks = ['사용빈도 1억 먹자 영어표현']

chromedriver_path = 'D:\\mine\\python\\toy\\chromedriver'
naver_id = 'ivvve'
naver_pw = 'sycive2'

driver = webdriver.Chrome(chromedriver_path)
driver.implicitly_wait(3)

# 접속 후 네이버 로그인 페이지로 이동
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

# 로그인
## Capcha 적용으로 인한 input
while True:
    print('로그인 후 y를 입력해주세요')
    y = input()
    if y == 'y':
        break
    else:
        print('y를 입력해야 다음 단계로 넘어갑니다.')

# 카페 접속
driver.get('https://cafe.naver.com/superenglishcafe')
title = driver.title

if title.index('마유영어') < 0:
    print('카페에 접속이 되지 않았네요...')
    exit(1)

# greeting
print('\n\n#######################')
print('Welcome to Mayu English')
print('#######################')

# 스터디 스케줄/컨텐츠로 이동
driver.execute_script('document.getElementById("menuLink319").click()')
# driver.find_element_by_id('menuLink319').click()
# find_element_by_css_selector('#cafe-menu #group303 #menuLink319').
title = driver.title

if title.index('스케줄/컨텐츠') < 0:
    print('스터디/컨텐츠 페이지로 접속이 되지 않았네요...')
    exit(2)

print("Let's check it out!")

homework_list_page = BeautifulSoup(driver.page_source, 'html.parser')
homework_board_list = homework_list_page.select('#main-area > div:nth-child(5) > table > tbody > tr')

# iframe으로 들어가기
driver.switch_to_frame(driver.find_element_by_id('cafe_main'))

board = driver.find_elements_by_css_selector('.article-board')[1]
article_list = board.find_elements_by_class_name('td_article')

homework_url_list = {}

for article in article_list:
    title = article.find_element_by_class_name('article');
    title_str = title.text
    homework_url_list[title.text] = title.get_attribute('href')

# iframe 나가기

for title, url in homework_url_list.items():
    print(title, ':', url)

driver.switch_to_default_content()


