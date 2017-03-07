# -- coding: UTF-8 --

import requests
import time


def main():
    start_time = time.time()
    url = "http://CepheusSun.com"
    for i in range(100):
        get_the_html(url)
    end_time = time.time()
    print(end_time - start_time)


def get_the_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('there is something wrong!')


if __name__ == '__main__':
    main()
