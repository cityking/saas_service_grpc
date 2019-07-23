import requests
import hashlib
import json

def str_md5(string):
    md = hashlib.md5()
    md.update(string.encode())
    res = md.hexdigest()
    return res

def query_calendar(year, month):
    year = str(year)
    month = str(month)

    if month.startswith('0'):
        month = month[-1]

    checkValue = str_md5(year+month).upper()
    url = 'http://site.zhibeili.com/index.php?g=app&m=Zangli&a=index'
    data = json.dumps(dict(year=year,month=month)) 
    data = dict(checkValue=checkValue,
        data=data)
    res = requests.post(url, data=data).content.decode()
    print(res)

query_calendar(2019, 9)

