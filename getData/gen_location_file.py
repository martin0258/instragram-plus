import instagramUtil
def read_data(filename):
    with open(filename,'r') as f:
        lines_token = [line[:-1].split(',') for line in f.readlines()]
        #                  [location_id  [other value]]
        data_list = [(line[0],line[1:]) for line in lines_token]
    return data_list

def main(args):


    try:
        src_filename = args[0]
        des_filemname = args[1]
    except:
        raise SystemExit('please input filename')


    location_list = read_data(src_filename)
    print 'read data done'
    count = 1
    data_len = len(location_list)
    with open(des_filemname,'w') as f :
        for location in location_list:
            print str(count)+'/'+str(data_len)
            result = instagramUtil.get_location_all_media(api,location[0])
            tmp_str = location[0]+','+location[1][2]+','+str(len(result))+'\n'
            f.write(tmp_str)
            count += 1

if __name__ == "__main__":
    main(sys.argv[1:])