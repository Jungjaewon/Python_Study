import requests
import json
# Ref 1 : https://brownbears.tistory.com/198

def http_get_example():
    print('-' * 5 + 'http_get_example' + '-' * 5)
    url = 'https://google.com'
    reponse = requests.get(url)
    print('reponse.status_code : ', reponse.status_code)
    print('reponse.text : ', reponse.text)
    print('reponse.json() : ', reponse.json())

    # pass the parameters

    com_code = '1234'
    params = {'code' : com_code}
    res = requests.get(url='https://localhost/test', params=params)
    print('res.json() : ', res.json())
    print('res.url : ', res.url)


def http_post_example():
    print('-' * 5 + 'http_post_example' + '-' * 5)
    com_code = '1234'
    params = {'code': com_code}
    url = 'https://localhost/test'
    response = requests.post(url, data=params)
    #response = requests.post(url, data=json.dump(params))
    print('response.json : ',response.json())


def http_header_cookie_timeout_example():
    print('-' * 5 + 'http_header_cookie_timeout_example' + '-' * 5)
    url ='https://localhost/test'
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    cookies = {'id' : 'WJEJGJ9231M1RR2OP'}
    response = requests.get(url=url, headers=headers, cookies=cookies, timeout=1)
    print('reponse.status_code : ', response.status_code)
    print('reponse.text : ', response.text)
    print('response.json : ', response.json())
    print('response.url : ', response.url)

if __name__ == '__main__':
    http_get_example()
    http_post_example()
    http_header_cookie_timeout_example()

