from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError
from pprint import pprint
from time import sleep
from operator import itemgetter
import os.path
import pickle
def main():
    #get an access token
    #get the api list at https://github.com/Instagram/python-instagram
    #detail at http://instagram.com/developer/endpoints
    
    #jimmy
    access_token = "1281386577.1fb234f.7f92a2ee25e447c592e1f54a66e21faa"
    target_user_id = 1281386577

    #louis
    #access_token = "344818875.e56c4b8.8f6d96561a5d4e7a91d98018432f4542"
    #target_user_id = 344818875

    api = InstagramAPI(access_token=access_token)

    
    steps = 2
    users_list = get_target_user_list(api,target_user_id, steps=steps)
    print str(steps)+" steps gets "+str(len(users_list))+" users"
    print "start crawling user media"
    #get_popular_media(api)
    count = 0

    media_list = []
    for user_id in users_list:
        print "progress "+str(count)+"/"+str(len(users_list))+ "now:"+str(user_id)
        media = get_user_all_media(api,user_id)
        for medium in media:
            medium_tmp = {'id':medium.id,'time':medium.created_time,'liker':[]}
            for liker in get_media_likes(api,medium.id):
                medium_tmp['liker'].append(liker.id)
            media_list.append(medium_tmp)
        count += 1
    media_list  = sorted(media_list, key=itemgetter('time')) 
    with open('output_like_api.txt','w') as f:
        for medium in media_list:
            tmp_string = "%s:%s\n" % ( str(medium['id']), ','.join(medium['liker']) )
            f.write(tmp_string)
def get_target_user_list(api,user_id,steps=2):
    fname = "tmp_data/get_target_user_list"+str(user_id)+"_"+str(steps)
    if os.path.isfile(fname):
        with open(fname,'rb') as f:
            user_list = pickle.load(f)
        return user_list

    follows_list = get_all_user_target_follows(api,user_id)
    #should we include the users who follow the target user
    followed_by_list = get_all_user_followed_by(api,user_id)
    to_be_crawl_user = follows_list | followed_by_list
    user_list = to_be_crawl_user
    print "tmp_data/get target user step 1 done"
    no_auth_user_list = set()

    for step in range(1,steps):
        print "in step "+str(step)
        count = 0

        tmp_user_list = set()
        for user in to_be_crawl_user:
            user_target = get_all_user_target_follows(api,user)
            #should we include the users who follow the target user
            user_followed = get_all_user_followed_by(api,user)
            if user_target == None or user_followed == None:
                no_auth_user_list.add(user)
            else:
                tmp_user_list |= user_target
                tmp_user_list |= user_followed
            count += 1
            print "progress "+str(count)+"/"+str(len(to_be_crawl_user))

        tmp_user_list.discard(user_id)
        to_be_crawl_user = tmp_user_list-user_list

        if len(to_be_crawl_user) == 0:
            break;
        user_list |= to_be_crawl_user
    with open(fname,'wb') as f:
        pickle.dump(user_list,f)
    return user_list
#to-do try
def get_all_user_target_follows(api,target_id):
    fname = "tmp_data/get_all_user_target_follows"+str(target_id)
    if os.path.isfile(fname):
        with open(fname,'rb') as f:
            result = pickle.load(f)
        return result
    result = set()
    next = None
    while True:
        while True:
            try:
                users, next = api.user_follows(target_id,with_next_url=next)
                break
            except InstagramAPIError as e:
                if e.status_code ==400:
                    users = []
                    next = None
                    break
                else:
                    print e
                    sleep(600)
            except:
                pass
        for user in users:
            result.add(user.id)
        if next == None:
            break
    with open(fname,'wb') as f:
        pickle.dump(result,f)
    return result
def get_all_user_followed_by(api,target_id):
    fname = "tmp_data/get_all_user_followed_by"+str(target_id)
    if os.path.isfile(fname):
        with open(fname,'rb') as f:
            result = pickle.load(f)
        return result

    result = set()
    next = None
    while True:
        while True:
            try:
                users, next = api.user_followed_by(target_id,with_next_url=next)
                break
            except InstagramAPIError as e:
                if e.status_code == 400:
                    users = []
                    next = None
                    break
                else:
                    print e
                    sleep(600)
            except:
                pass
        for user in users:
            result.add(user.id)
        if next == None:
            break
    with open(fname,'wb') as f:
        pickle.dump(result,f)
    return result

def get_user_all_media(api,target_id):
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
def get_media_likes(api,medium_id):
    fname = "tmp_data/get_media_likes"+str(medium_id)
    if os.path.isfile(fname):
        with open(fname,'rb') as f:
            media = pickle.load(f)
            if media == None:
                return []
        return media
    while True:
        try:
            media = api.media_likes(medium_id)
            break;
        except InstagramAPIError as e:
            if e.status_code == 400:
                media = []
                break
            else:
                print e
                sleep(600)
        except :
            print "error medium_id = "+str(medium_id)
    with open(fname,'wb') as f:
        pickle.dump(media,f)
    return media


def crawl_user(api):
    crawlable_user = []
    for user_id in range(0,1000):
        try:
            api.user(user_id)
            crawlable_user.append(user_id)
        except:
            print user_id
            continue
    return crawlable_user
if __name__ == '__main__':
    main()


