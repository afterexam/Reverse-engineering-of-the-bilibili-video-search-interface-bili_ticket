

import requests
from get_ck import get_ck

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://search.bilibili.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://search.bilibili.com/all",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}



def main(i):
    cookies = {
        "bili_ticket": get_ck(),

    }
    url = "https://api.bilibili.com/x/web-interface/wbi/search/all/v2"
    params = {
        "page": i,
        "keyword": "原神启动",

    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
    # print(response)
    try:
        video_list = response['data']['result'][11]['data']
        print(len(video_list))
        for i in video_list:
            print(f"{i['title']}     作者: {i['author']}")

    except:
        print(response)

# print(response)
if __name__ == '__main__':
    for i in range(1,100):
        main(i)
