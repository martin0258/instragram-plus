from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError
from time import sleep
import os.path
import pickle
import random
__access_token_list =                                                                                 \
["1281386577.1fb234f.7f92a2ee25e447c592e1f54a66e21faa",
"1364879630.1fb234f.66ba2d2c37494f26b06255a916fc5874",
"1364881954.9799c21.0d78158b4bf147e697c388d710946715",
"1364881954.e184e8f.e5d5732651184f24ba1a67d37f79a206",]
__access_token_index = random.randrange(len(__access_token_list))
__api = None

def __initAPI():
    __api = InstagramAPI(access_token=__access_token_list[__access_token_index])
def __switch_access_token():
    __access_token_index = random.randrange(len(__access_token_list))
    __api = InstagramAPI(access_token=__access_token_list[__access_token_index])
def get_user_all_media(target_id,count=-1,max_time):
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
                    print "access_token_index "+str(__access_token_index)+"is out of limit request"
                    __switch_access_token()
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
                    print "access_token_index "+str(__access_token_index)+"is out of limit request"
                    __switch_access_token()
            except:
                count = 100000
                pass
        result += recent_media
        if next == None:
            break
    with open(fname,'wb') as f:
        pickle.dump(result,f)
    return result  

__initAPI()
"""    
    jimmy
    access_token = "1281386577.1fb234f.7f92a2ee25e447c592e1f54a66e21faa"

    louis
    access_token = "344818875.e56c4b8.8f6d96561a5d4e7a91d98018432f4542"
    target_user_id = 344818875
"""