from bs4 import BeautifulSoup
import requests
import json

from .sdvx import Chart, SkillCourse

def download_page_as_soup(url):
    page = requests.get(url)
    content = page.content.decode('euc_jp', errors='ignore')

    return (BeautifulSoup(content, 'html.parser'))

def get_courses_tables(soup):
    result = []

    for table in soup.find(id='body').find_all('table'):
        if table.find('td', string='TRACK') is not None:
            result.append(table)
    return result

def get_courses(soup, title='Other'):
    result = []
    count = 0

    for tr in soup.tbody.find_all('tr'):
        if count == 0:
            course = SkillCourse()
            course.name = title
            course.dai = tr.td.strong.contents[0]
        else:
            tds = tr.find_all('td')
            chart = Chart()
            chart.song_title = tds[1].contents[0]
            chart.difficulty = tds[2].strong.contents[0]
            chart.level = tds[3].contents[0]
            course.charts.append(chart)
        if count < 3:
            count += 1
        else:
            result.append(course)
            count = 0
    return result

def tables_to_courses(soup):
    result = []

    for table in soup:
        if len(table.thead.find_all('tr')) == 2 \
        and len(table.thead.tr.find_all('td')) == 1:
            header = table.thead.tr.td.contents
            title = '{} {}'.format(header[0].strip(), header[1].contents[0].strip())
            result += get_courses(table, title=title)
        else:
            result += get_courses(table)
    return result
