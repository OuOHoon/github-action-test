import datetime
import json
import re
import random
from problem_crawler import crawling


# 최초 1회차는 미리 정해져 있어야함
def update(p):
    with open("README.md", "r") as f:
        pattern = r"\d+"
        match = re.search(pattern, f.readlines()[-1])
        n = match.group()
    with open("README.md", "a+") as f:
        today = datetime.date.today()
        template = f"\n| {int(n) + 1}회차({today.year}.{today.month}.{today.day}) | [{p['title']}](https://school.programmers.co.kr/learn/courses/30/lessons/{p['id']})|"
        f.write(template)


# 랜덤으로 안 푼 문제 하나 뽑음
def choose_one():
    with open("problems.json", "r") as f:
        problems = json.load(f)
        problem = problems[random.randrange(len(problems))]
        while problem.get('solved', False):
            problem = problems[random.randrange(len(problems))]
        problem['solved'] = True
    with open("problems.json", "w") as f:
        json.dump(problems, f, indent=4)
    return problem


if __name__ == '__main__':
    try:
        with open("problems.json", "r") as f:
            pass
    except:
        crawling()
    update(choose_one())
