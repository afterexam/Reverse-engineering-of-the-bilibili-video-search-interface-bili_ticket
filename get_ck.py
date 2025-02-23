import requests

import hmac
import hashlib
from main_site import get_b_nut

def calculate_hmac(e):
    key = "XgwSnGZ1p"
    # 构造消息，相当于JavaScript中的 `ts${e}`
    message = f"ts{e}"
    # 使用HMAC SHA256算法计算哈希
    digest = hmac.new(
        key.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    )
    # 转换为十六进制字符串
    return digest.hexdigest()

# 示例用法
b_nut = get_b_nut()
r = calculate_hmac(b_nut)
# print(r)

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-length": "0",
    "origin": "https://search.bilibili.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://search.bilibili.com/all?vt=00024882&keyword=%E6%88%91%E8%A6%81%E7%8E%A9%E5%8E%9F%E7%A5%9E&from_source=webtop_search&spm_id_from=333.1007&search_source=5",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

url = "https://api.bilibili.com/bapis/bilibili.api.ticket.v1.Ticket/GenWebTicket"
params = {
    "key_id": "ec02", # 固定
    "hexsign": r, # 加密,和b_nut有关
    "context[ts]": b_nut, # 在主站接口返回的ck上b_nut
    "csrf": ""
}
def get_ck():
    response = requests.post(url, headers=headers,params=params).json()
    return response['data']['ticket']

if __name__ == '__main__':
    a = get_ck()
    print(a)