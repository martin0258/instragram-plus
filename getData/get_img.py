import urllib
import instagramUtil
import os.path
import os
import pickle
def read_data(fname='temp_location.txt'):
    with open(fname,'r') as f:
        return [line.strip().split(',') for line in f.readlines()]

def get_img(url,fname):
    if os.path.isfile(fname):
        return
    with open(fname,'wb') as f:
        f.write(urllib.urlopen(url).read())

def get_represent_img(f,data_list):
    count = 1
    data_num = len(data_list)
    for data in data_list:
        result = instagramUtil.get_location_all_media(data[0].strip())
        if len(result) >0:
            result = result[0]
            url = result.images['thumbnail'].url
            fname = data[0].strip()+'.jpg'
            get_img(url, 'img/'+fname)
            tmp_str = fname+':'+','.join(data[1:3])+'\n'
            f.write(tmp_str)
        print str(count)+'/'+str(data_num)
        count +=1
def get_location_img(location_id):
    result = instagramUtil.get_location_all_media(location_id)
    data_num = len(result)
    count = 1
    directory_name = 'img_'+str(location_id)
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)
    for data in result:
        print str(count)+'/'+str(data_num) 
        url = data.images['thumbnail'].url
        fname = directory_name+'/'+str(count)+'.jpg'
        get_img(url,fname)
        count +=1
    return 
def main(): 

    #Taipei Expo Park
    get_location_img(32820)
    """
    data_list = read_data()
    print 'read done'
    with open('img_list.txt','w') as f:
        get_represent_img(f,data_list)
    """
if __name__ == '__main__':
    main()