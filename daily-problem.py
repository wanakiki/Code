import requests
import json
import re
import time

Remove = [
    "</?p>",
    "</?ul>",
    "</li>",
    "\\t",
    "</?ol>"
]
Replace = [
    ["&#39;", "'"],
    ["&quot;", '"'],
    ["&lt;", "<"],
    ["&gt;", ">"],
    ["&nbsp;", " "],
    ["</?code>", "``"],
    ["</?strong>", "**"],
    ["\s</?em>", "*"],
    ["<pre>", "```\n"],
    ["</pre>", "```"],
    ["<li>", "- "],
    ["<br />", "\n"],
    ["<br>", "\n"],
]


def convert(src):
    # pre内部预处理
    # span = re.search("<pre>[\s\S]*</pre>", src).span()
    # tmp = re.sub("<[^>p]*>", "", src[span[0]: span[1]])     # 不含有p的标签
    # print(tmp)
    # src = re.sub("<pre>[\s\S]*?</pre>", tmp, src)
    def remove_label_in_pre(matched):
        tmp = matched.group()
        tmp = re.sub("<[^>p]*>", "", tmp)   # 不匹配>与p
        return tmp
    src = re.sub("<pre>[\s\S]*?</pre>", remove_label_in_pre,
                 src)   # 注意此处非贪心匹配，因为可能有多个示例
    for curPattern in Remove:
        src = re.sub(curPattern, "", src)

    for curPattern, curRepl in Replace:
        src = re.sub(curPattern, curRepl, src)
    return src


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
session = requests.Session()


def get_problem_content(slug):
    url = "https://leetcode-cn.com/graphql"
    params = {'operationName': "getQuestionDetail",
              'variables': {'titleSlug': slug},
              'query': '''query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionFrontendId
                difficulty
                translatedTitle
                translatedContent
            }
        }'''
              }
    json_data = json.dumps(params).encode('utf8')

    headers = {'User-Agent': user_agent, 'Connection':
               'keep-alive', 'Content-Type': 'application/json',
               'Referer': 'https://leetcode-cn.com/problems/' + slug}
    resp = session.post(url, data=json_data, headers=headers, timeout=10)
    resp.encoding = 'utf8'
    content = resp.json()
    # print(content)
    question = content['data']['question']
    question_id = question['questionFrontendId']
    question_title = question['translatedTitle']
    question_content = convert(question['translatedContent'])
    question_difficulty = question['difficulty']
    res = f"""## {question_id}. {question_title}

{time.strftime("%Y-%m-%d %X", time.localtime())}

### 题目

{question_content}

[LeetCode链接]({"https://leetcode-cn.com/problems/" + slug + "/"})

### 思路及代码
"""
    
    f_name = question_id + '-' + slug + '.md'
    if question_difficulty == 'Medium':
        f_name = "leetcode_medium/" + f_name
        with open(f_name, 'w', encoding='utf8') as fh:
            fh.write(res)
    elif question_difficulty == 'Easy':
        f_name = "leetcode_easy/" + f_name
        with open(f_name, 'w', encoding='utf8') as fh:
            fh.write(res)
    elif question_difficulty == 'Hard':
        f_name = "hard/" + f_name
        with open(f_name, 'w', encoding='utf8') as fh:
            fh.write(res)
    else:
        print(content)
        print(res)

def get_daily_slug() -> str:
    """获取每日一题的slug"""
    # https://blog.csdn.net/malloc_can/article/details/113004579
    response = requests.post("https://leetcode-cn.com/graphql", json={
        "operationName": "questionOfToday",
        "variables": {},
        "query": "query questionOfToday { todayRecord {   question {     questionFrontendId     questionTitleSlug     __typename   }   lastSubmission {     id     __typename   }   date   userStatus   __typename }}"
    })
    daily_slug = json.loads(response.text).get('data').get('todayRecord')[0].get("question").get('questionTitleSlug')
    
    return daily_slug

str = "https://leetcode-cn.com/problems/remove-k-digits/"
str = str.split('/')[-2]
# print(get_daily_slug())
# get_problem_content("minimum-recolors-to-get-k-consecutive-black-blocks")
get_problem_content(slug=get_daily_slug())
