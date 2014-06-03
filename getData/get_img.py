import urllib
from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError
import os.path
import pickle
def get_location_all_media(api,target_id):
    fname = "tmp_data/get_location_all_media_"+str(target_id)
    if os.path.isfile(fname):
        return []
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
def read_data(fname='temp_location.txt'):
    with open(fname,'r') as f:
        return [line.strip().split(',') for line in f.readlines()]

def get_img(url,fname):
    if os.path.isfile(fname):
        return
    with open(fname,'wb') as f:
        f.write(urllib.urlopen(url).read())

def get_represent_img(api,f,data_list):
    count = 1
    data_num = len(data_list)
    for data in data_list:
        result = get_location_all_media(api,data[0].strip())
        if len(result) >0:
            result = result[0]
            url = result.images['thumbnail'].url
            fname = data[0].strip()+'.jpg'
            get_img(url, 'img/'+fname)
            tmp_str = fname+':'+','.join(data[1:3])+'\n'
            f.write(tmp_str)
        print str(count)+'/'+str(data_num)
        count +=1
def main(): 
    access_token = "1281386577.1fb234f.7f92a2ee25e447c592e1f54a66e21faa"
    api = InstagramAPI(access_token=access_token)
    data_list = read_data()
    print 'read done'
    with open('img_list.txt','w') as f:
        get_represent_img(api,f,data_list)
if __name__ == '__main__':
    main()