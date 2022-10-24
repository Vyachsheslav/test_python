from urllib import response
import requests
from pprint import pprint
import yadisk



TOKEN = "AQAEA7qj0SyLAADLWxJK0PtrYUrqkqZl0aVPcxY"

def ya_api(name):
    ya = yadisk.YaDisk(token=TOKEN)
    ya.mkdir('test')
    ya.mkdir(f'test/{name}')

    list_files = (list(ya.listdir("/test")))
    return list_files[0]['name']

def delete_fold():
    ya = yadisk.YaDisk(token=TOKEN)
    ya.remove(f"/test", permanently=True)






