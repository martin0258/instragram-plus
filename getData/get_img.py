import urllib
import instagramUtil
import location_base
import os.path
import os
import pickle

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
    directory_name = 'all_img/img_'+str(location_id)
    count = 1
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)
        for data in result:
            url = data.images['thumbnail'].url
            fname = directory_name+'/'+str(count)+'.jpg'
            get_img(url,fname)
            count +=1

    
    fname = directory_name+'/info.txt'
    with open(fname,'w') as f:
        for data in result:
            attribute = []
            attribute.append(data.link.split('/')[-2])
            attribute.append(str(data.like_count))
            if hasattr(data, 'tags'):
                attribute.append(' '.join(tag.name for tag in data.tags))
            else:
                attribute.append('')
            attribute.append(data.images['standard_resolution'].url)
            #photo id
            tmp_str = ','.join(attribute)+'\n'
            f.write(tmp_str.encode('utf-8'))
    return
def get_all_location_img_from_file(fname):
    location_list = location_base.read_location_data(fname)
    count = 1
    lenth = len(location_list)
    for location in location_list:
        print "%d / %d" %(count,lenth)
        get_location_img(location['id'])
        count += 1
def get_top_15_location_img():
    location_list = [32820,50594,9496078,687587,113224417,11132,39267,37593,28660,12144,16470,212795,2108091,12302,31362592,51726]
    count = 1
    lenth = len(location_list)
    for location in location_list:
        print "%d / %d" %(count,lenth)
        get_location_img(location['id'])
        count += 1
def main(): 
        #get_top_15_location_img
        get_all_location_img_from_file("location.txt")

if __name__ == '__main__':
    main()
