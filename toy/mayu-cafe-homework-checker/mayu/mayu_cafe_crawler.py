from selenium import webdriver
from my_date import my_date

from bs4 import BeautifulSoup

def get_driver(chrome_driver_path):
    driver = webdriver.Chrome(chrome_driver_path)
    driver.implicitly_wait(3)
    return driver

def naver_login(driver):
    driver.get('https://nid.naver.com/nidlogin.login')

    while True:
        print('로그인 후 y를 입력해주세요')
        y = input()

        if y == 'y':
            break
        else:
            print('y를 입력해야 다음 단계로 넘어갑니다.')

def enter_board_iframe(driver):
    driver.switch_to_frame(driver.find_element_by_id('cafe_main'))


def simeple_homework_articles_of_month(iframe_driver):
    homework_board = iframe_driver.find_elements_by_css_selector('.article-board')[1]
    homework_articles = homework_board.find_elements_by_class_name('td_article')

    simple_homework_articles = {}
    month = my_date.month().upper()

    for homework_article in homework_articles:
        homework_article = homework_article.find_element_by_class_name('article')
        homework_title = homework_article.text

        # 프로필, 스케쥴은 건너 뛴다
        if homework_title.startswith('[일정]') or (homework_title.find('멤버 프로필') >= 0):
            continue

        # 이번 달 외에는 담지 않는다.
        if homework_title.upper().find(month) >= 0:
            break

        homework_link = homework_article.get_attribute('href')
        simple_homework_articles[homework_title] = homework_link

    return simple_homework_articles

def simple_comments_of_article(article_driver):
    comments = article_driver.find_elements_by_css_selector('#main-area #cmt_list > li:nth-child(odd)')
    simple_comments = {}

    for comment in comments:
        name = comment.find_element_by_css_selector('.p-nick').text
        content = comment.find_element_by_css_selector('.comm_body').text
        simple_comments[name] = content

    return simple_comments
