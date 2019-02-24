import mayu.mayu_cafe_crawler as my_hw
from mayu.User import *

user_names = ['ChrisSon', '박나현 Betty', 'Chloe']
users = {
    'ChrisSon': [],
    '박나현 Betty': [],
    'Chloe': []
}

################################################

chrome_driver_path = 'D:\\mine\\python\\toy\\chromedriver'

driver = my_hw.get_driver(chrome_driver_path)
# my_hw.naver_login(driver)

# 카페 접속
driver.get('https://cafe.naver.com/superenglishcafe')

if driver.title.find('마유영어') < 0:
    print('You are not in the cafe')
    exit(1)

# 스터디 스케쥴/컨텐츠로 이동
driver.execute_script('document.getElementById("menuLink319").click()')

if driver.title.find('스케줄/컨텐츠') < 0:
    print('You are not in the 스터디/컨텐츠 페이지')
    exit(2)

my_hw.enter_board_iframe(driver)
homework_articles = my_hw.simeple_homework_articles_of_month(driver)

print('-------------------------------')
print('숙제 목록')
for k, v in homework_articles.items():
    print(k, v)
print('-------------------------------')

for title, uri in homework_articles.items():
    driver.get(uri)
    my_hw.enter_board_iframe(driver)
    comments = my_hw.simple_comments_of_article(driver)

    for name, comment in comments.items():
        # print('------------------------------')
        # print(author)
        # print(comment)
        # print('------------------------------')
        if name in user_names:
            users[name].append({
                title: comment
            })

for k, v in users.items():
    print(k, '숙제 횟수: ', len(v))
    for i in v:
        print(i)