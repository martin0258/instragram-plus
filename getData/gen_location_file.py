from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError
from time import sleep
from operator import itemgetter
import os.path
import pickle
import sys
def read_data(filename):
    with open(filename,'r') as f:
        lines_token = [line[:-1].split(',') for line in f.readlines()]
        #                  [location_id  [other value]]
        data_list = [(line[0],line[1:]) for line in lines_token]
    return data_list
def get_location_all_media(api,target_id):
    fname = "tmp_data/get_location_all_media_"+str(target_id)
    if os.path.isfile(fname):
        with open(fname,'rb') as f:
            result = pickle.load(f)
        return result

    result = []
    next = None

    while True:
        while True:
            try:
                recent_media, next = api.location_recent_media(count=-1,location_id=target_id, with_next_url=next)
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
        result += recent_media
        if next == None:
            break
    with open(fname,'wb') as f:
        pickle.dump(result,f)
    return result    
def main(args):


    try:
        src_filename = args[0]
        des_filemname = args[1]
    except:
        raise SystemExit('please input filename')
    #jimmy
    access_token = "1281386577.1fb234f.7f92a2ee25e447c592e1f54a66e21faa"

    #louis
    #access_token = "344818875.e56c4b8.8f6d96561a5d4e7a91d98018432f4542"
    #target_user_id = 344818875

    api = InstagramAPI(access_token=access_token)
    location_list = read_data(src_filename)
    print 'read data done'
    count = 1
    data_len = len(location_list)
    with open(des_filemname,'w') as f :
        for location in location_list:
            print str(count)+'/'+str(data_len)
            result = get_location_all_media(api,location[0])
            tmp_str = location[0]+','+location[1][2]+','+str(len(result))+'\n'
            f.write(tmp_str)

if __name__ == "__main__":
    main(sys.argv[1:])