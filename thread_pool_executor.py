'''
concurrent.future线程池的用法
'''

from concurrent.futures import ThreadPoolExecutor
import requests

urls = [
    'https://liyuankun.cn',
    'https://www.baidu.com',
    'https://github.com'
]

def fetch_url(url):
    req = requests.get(url, timeout=60)
    print(f'{url} page is {len(req.content)} bytes.')

with ThreadPoolExecutor(max_workers=3) as pool:
    pool.map(fetch_url, urls)

