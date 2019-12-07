import urllib.request

if __name__ == '__main__':
    print('-' * 5 + 'urllib.request example' + '-' * 5)
    a = urllib.request.urlopen("http://www.google.com/")
    # read is a one time usaged
    # when read all data,
    print('a.read() : ', a.read())
    a = urllib.request.urlopen("http://www.google.com/")
    print('a.read().decode("utf-8") : ', a.read().decode("utf-8"))

