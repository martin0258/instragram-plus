from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError
from time import sleep
import os.path
import pickle

def initAPI():
    access_token = "1281386577.1fb234f.7f92a2ee25e447c592e1f54a66e21faa"
    return InstagramAPI(access_token=access_token)

def get_user_all_media(target_id):
    fname = "tmp_data/get_user_all_media"+str(target_id)
    if os.path.isfile(fname):
        with open(fname,'rb') as f:
            result = pickle.load(f)
        return result

    result = []
    next = None

    while True:
        while True:
            try:
                recent_media, next = api.user_recent_media(user_id=target_id, with_next_url=next)
                break
            except InstagramAPIError as e:
                if e.status_code == 400:
                    recent_media = []
                    next = None
                    break
                else:
                    print e
                    sleep(600)
            except:
                pass
        result += recent_media
        if next == None:
            break
    with open(fname,'wb') as f:
        pickle.dump(result,f)
    return result

def get_location_all_media(target_id):
    fname = "tmp_data/get_location_all_media_"+str(target_id)
    if os.path.isfile(fname):
        with open(fname,'rb') as f:
            result = pickle.load(f)
        return result
    result = []
    next = None
    count = -1
    while True:
        while True:
            try:
                recent_media, next = api.location_recent_media(count=count,location_id=target_id, with_next_url=next)
                print 'get:'+str(len(recent_media))+' media'
                break
            except InstagramAPIError as e:
                if e.status_code == 400:
                    recent_media = []
                    next = None
                    break
                else:
                    print e
                    sleep(600)
            except:
                count = 100000
                pass
        result += recent_media
        if next == None:
            break
    with open(fname,'wb') as f:
        pickle.dump(result,f)
    return result   
api = initAPI()
"""    
    jimmy
    access_token = "1281386577.1fb234f.7f92a2ee25e447c592e1f54a66e21faa"

    louis
    access_token = "344818875.e56c4b8.8f6d96561a5d4e7a91d98018432f4542"
    target_user_id = 344818875
"""