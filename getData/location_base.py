import instagramUtil
import pickle
import sys
def read_location_data(fname):
    with open(fname,'r') as f:
        lines_token = [line[:-1].split(',') for line in f.readlines()]
        #                  [location_id  [other value]]
        data_list = [ {'id':line[0],'lat':line[1],'lon':line[2],'name':line[3],'count':line[4]} for line in lines_token]
    return data_list
def read_location_results_from_pickle(fname):
    with open(fname,'rb') as f:
        return pickle.load(f)

def get_locations_media(location_list):
    count = 1
    data_len = len(location_list)
    results = []
    for location in location_list:
        print str(count)+'/'+str(data_len)
        result = {}
        medium = instagramUtil.get_location_all_media(location['id'])
        result['medium'] = medium
        result['id'] = location['id']
        result['lat'] = location['lat']
        result['lon'] = location['lon']
        result['name'] = location['name']
        results.append(result)
        count += 1
    return results
#gen location file. format: id,name,media_count
def output_location_results(fname,location_results):
    locations = []
    for location in location_results:
        attribute =[]
        attribute.append(location['id'])
        attribute.append(location['lat'])
        attribute.append(location['lon'])
        attribute.append(location['name'])
        attribute.append(str(len(location['medium'])))
        locations.append(attribute)
    locations = sorted(locations,key = lambda x:x[4], reverse =True)
    with open(fname,'w') as f :
        for attribute in locations:
            tmp_str =','.join(attribute)+'\n'
            f.write(tmp_str)
    return True
def output_location_results_to_pickle(fname,location_results):
    with open(fname,'wb') as f :
        pickle.dump(location_results,f)
    return True
def get_user_info(user_list):
    results = {}
    num_sum = len(user_list)
    count = 1
    for u_id in user_list:
        print str(count)+'/'+str(num_sum)
        results[u_id] = instagramUtil.get_user_all_media(target_id = u_id,count=1000,save_time=True)
        count += 1
    return results

def read_user_list_data(fname="location_img_user_id.txt"):
    with open(fname,'r') as f:
        user_list = [line[:-1] for line in f.readlines()]
    return user_list

def get_locations_media_user_info(location_results):
    results = {}
    img_num_sum = sum([len(location['medium']) for location in location_results])
    count = 1
    for location in location_results:
        for media in location['medium']:
            print str(count)+'/'+str(img_num_sum)
            results[media.user.id] = instagramUtil.get_user_all_media(target_id = media.user.id,count=1000)
            count += 1
    return results

def output_user_list_from_location(fname="location_img_user_id.txt",location_results=[]):
    results = {}
    count = 1
    for location in location_results:
        for media in location['medium']:
            results[media.user.id] = 1
    with open(fname,'w') as f:
        for user in results:
            print str(count)+'/'+str(len(results))
            tmp_str = str(user)+'\n'
            count += 1
            f.write(tmp_str)
    return True
def is_in_taiwan(lon,lat):
    return lon<122 and lon >119 and lat < 25.5 and lat >21.5
def output_user_guess_list():
    user_list = read_user_list_data()
    num_sum = len(user_list)
    count = 1    
    with open('user_guess.txt','w') as f:
        for u_id in user_list:
            count_y = 0
            count_n = 0
            print str(count)+'/'+str(num_sum)
            try:
                for media in instagramUtil.get_user_all_media(target_id = u_id):
                    if hasattr(media,'location') and media.location != None and media.location.point != None:
                        if is_in_taiwan(lon= media.location.point.longitude,lat=media.location.point.latitude):
                            count_y += 1
                        else:
                            count_n += 1
                if count_y > count_n:
                    tmp_str = "%s,%d,%d\n" % (u_id,1,count_y+count_n)
                elif count_y == count_n:
                    tmp_str = "%s,%d,%d\n" % (u_id,0,count_y+count_n)
                else:
                    tmp_str = "%s,%d,%d\n" % (u_id,-1,count_y+count_n)
                f.write(tmp_str)
            except:
                pass
            count += 1
    return
def get_user_info_job():
    user_list = read_user_list_data()
    get_user_info(user_list[::-1])
    
def output_location_image_created_time_info(location_results):

    for location in location_results:
        fname = 'img_time/'+location['id']+'.txt'
        f = open(fname,'w')
        for media in location['medium']:
            attribute = [media.created_time.year,media.created_time.month,media.created_time.day,media.created_time.hour,media.created_time.minute,media.created_time.second]
            attribute = [str(a) for a in attribute]
            tmp_string = ','.join(attribute)+'\n'
            f.write(tmp_string) 
        f.close()

def main(args):
    try:
        src_fname = args[0]
        des_fname = args[1]
    except:
        raise SystemExit('please input filename')

    
    #location_list = read_location_data(src_fname)
    print 'read data done'
    #location_results = get_locations_media(location_list)
    #location_results = read_location_results_from_pickle('location_results.pickle')
    #output_location_results(des_fname,location_results)
    #output_user_list_from_location(location_results=location_results)

    #-----get user_info----
    #get_user_info_job()
    #user_medium = get_locations_media_user_info(location_results)
    output_user_guess_list()


if __name__ == "__main__":
    main(sys.argv[1:])
