import requests
import json


def get_total_pages(url):
    response = requests.get(url + "1")
    if response.status_code == 200:
        data = json.loads(response.content)
        return data['totalPages']
    return 0


def get_programmers_level2_python3_problems(url, page):
    response = requests.get(url + str(page))
    if response.status_code == 200:
        data = json.loads(response.content)
        return data['result']
    return []


def crawling():
    url = "https://school.programmers.co.kr/api/v1/school/challenges/?perPage=50&levels[]=2&languages[]=python3&order=recent&search=&page="
    total_pages = get_total_pages(url)
    problems = []
    for i in range(1, total_pages + 1):
        problems.extend(get_programmers_level2_python3_problems(url, i))
    with open("problems.json", "w") as f:
        json.dump(problems, f, indent=4)


if __name__ == '__main__':
    crawling()
