import instagramUtil
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
        medium = instagramUtil.get_location_all_media(api,location['id'])
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
    user_list = {}
    for location in location_results:
        for media in location['medium']:
            user_list[media.user.id] = instagramUtil.get_user_all_media(media.user.id)
    return user_list
def main(args):
    try:
        src_fname = args[0]
        des_fname = args[1]
    except:
        raise SystemExit('please input filename')

    location_list = read_location_data(src_fname)
    print 'read data done'
    location_results = get_locations_media(location_list)
    
    #output_location_results(des_fnamem,location_results)


if __name__ == "__main__":
    main(sys.argv[1:])