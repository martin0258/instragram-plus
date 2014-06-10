import instagramUtil
import sys
def read_location_data(fname):
    with open(fname,'r') as f:
        lines_token = [line[:-1].split(',') for line in f.readlines()]
        #                  [location_id  [other value]]
        data_list = [ {'id':line[0],'lat':line[1],'lon':line[2],'name':line[3]} for line in lines_token]
    return data_list

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
        result['name'] = location['name']
        results.append(result)
        count += 1
    return results
#gen location file. format: id,name,media_count
def output_location_results(fname,location_results):
    with open(fname,'w') as f :
        for location in location_results:
            tmp_str = location['id']+','+location['name']+','+str(len(location['medium']))+'\n'
            f.write(tmp_str)
    return True
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

def main(args):
    try:
        src_fname = args[0]
        des_fname = args[1]
    except:
        raise SystemExit('please input filename')

    
    #location_list = read_location_data(src_fname)
    #print 'read data done'
    #location_results = get_locations_media(location_list)

    #output_user_list_from_location(location_results=location_results)
    user_list = read_user_list_data()
    get_user_info(user_list[::-1])
    #user_medium = get_locations_media_user_info(location_results)
    #output_location_results(des_fnamem,location_results)


if __name__ == "__main__":
    main(sys.argv[1:])
