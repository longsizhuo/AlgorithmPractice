import time

import requests
from bs4 import BeautifulSoup

# 2captcha API key
api_key = '6846cd644156a0d140c926faceb50bed'  # 替换为你的 2captcha API key

# 登录页面 URL
login_page_url = "https://www.globalinterpark.com/en/login"

# Captcha 请求 URL
captcha_request_url = "https://2captcha.com/in.php"
captcha_result_url = "https://2captcha.com/res.php"

# 登录请求 URL
login_url = "https://www.globalinterpark.com/api/sign-in/email"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
    "Origin": "https://www.globalinterpark.com",
    "Referer": "https://www.globalinterpark.com/en/login",
    "Sec-Ch-Ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "macOS",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sentry-Trace": "d95ee0eae9b245939df83dbe55817401-8e55c0ecf0949908-0",
    "X-Cbt-User-Lang": "en"
}

# 确认你从页面获取到正确的 sitekey
sitekey = "695da7821231"  # 替换为实际的 sitekey

# Captcha 请求所需的额外参数（如果适用）
cdata = "example_cdata"  # 替换为实际获取到的 cData
pagedata = "example_pagedata"  # 替换为实际获取到的 chlPageData
action = "example_action"  # 替换为实际获取到的 action

# 发送 Captcha 请求到 2captcha
captcha_payload = {
    'key': api_key,
    'method': 'turnstile',
    'sitekey': sitekey,
    'pageurl': login_page_url,
    'data': cdata,
    'pagedata': pagedata,
    'action': action,
    'json': 1
}

# 增加调试信息以确保请求正确
print("Captcha 请求 payload:", captcha_payload)

captcha_response = requests.post(captcha_request_url, data=captcha_payload)
captcha_response_json = captcha_response.json()
print("Captcha 请求响应:", captcha_response_json)
request_id = captcha_response_json.get('request')

if request_id and captcha_response_json.get('status') == 1:
    # 检查 Captcha 解析结果
    for i in range(10):
        result_payload = {
            'key': api_key,
            'action': 'get',
            'id': request_id,
            'json': 1
        }
        result_response = requests.get(captcha_result_url, params=result_payload)
        result_response_json = result_response.json()
        print(f"Captcha 解析结果: {result_response_json}")
        if result_response_json.get('status') == 1:
            token = result_response_json.get('request')
            print("获取到的 token:", token)

            # 登录表单数据
            login_data = {
                "email": "longsizhuo@gmail.com",  # 替换为你的用户名
                "password": "D^PNz+!kNJeJf8&",  # 替换为你的密码
                "token": token  # 从 2captcha 获取的 token
            }

            # 创建一个会话
            session = requests.Session()

            # 发送 POST 请求进行登录
            response = session.post(login_url, json=login_data, headers=headers, timeout=10)

            # 打印响应内容以进行调试
            print("响应状态码:", response.status_code)
            print("响应内容:", response.text)

            # 检查登录是否成功
            if response.status_code == 200:
                print("登录成功")

                # 获取账号信息页面 URL
                account_info_url = "https://www.globalinterpark.com/en/my-page"

                # 发送 GET 请求获取账号信息
                account_info_response = session.get(account_info_url, headers=headers, timeout=10)

                # 打印响应内容以进行调试
                print("账号信息页面响应状态码:", account_info_response.status_code)
                print("账号信息页面响应内容:", account_info_response.text)

                # 解析账号信息页面
                soup = BeautifulSoup(account_info_response.text, 'html.parser')

                # 提取账号信息
                try:
                    account_name = soup.find("div", {"class": "account-name"}).text.strip()
                    print("账号名称:", account_name)
                except AttributeError:
                    print("无法提取账号名称，请检查HTML结构")
                break
        else:
            time.sleep(5)
else:
    print("无法获取 request_id")
