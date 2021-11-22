import requests, json
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
    src = re.sub("<pre>[\s\S]*?</pre>", remove_label_in_pre, src)   # 注意此处非贪心匹配，因为可能有多个示例
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
                questionId
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
    question = content['data']['question']
    question_id = question['questionId']
    question_title = question['translatedTitle']
    question_content = convert(question['translatedContent'])
    res = f"""## {question_id}. {question_title}

{time.strftime("%Y-%m-%d %X", time.localtime())}

### 题目

{question_content}

[LeetCode链接]({"https://leetcode-cn.com/problems/" + slug + "/"})

### 思路及代码
"""
    return res


str = "https://leetcode-cn.com/problems/remove-k-digits/"
str = str.split('/')[-2]
res = get_problem_content("arranging-coins")
print(res)
