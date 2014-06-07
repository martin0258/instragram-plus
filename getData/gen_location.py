from urllib.parse   import quote
from urllib.request import urlopen
import urllib.request
import os.path
import pickle
import numpy
def get_location_result(lat,lon):
    fname = "tmp_data/location_"+str(lat)+"_"+str(lon)
    if os.path.isfile(fname):
        #speed up
        return []
        with open(fname,'rb') as f:
            results = pickle.load(f)
        return results
    while True:
        try:
            url = "http://maihamakyo.org/etc/locastagram/index.php?mode=search&latlng="+str(lat)+","+str(lon)
            response = urllib.request.urlopen(url)
            results = response.read().decode('utf-8')
            results = results[results.index('<table id="searchresult">'):]
            results = results[:results.index('</tr>\n\t\t</table>')]
            results = results.replace('\n','')
            results = results.replace('\t','')
            results = results.replace('</td>','')
            results = results.replace('</th>','')
            results = results.split('</tr><tr>')
            results = [a.split('<td>')[1:] for a in results[1:]]
            break
        except:
            pass
    with open(fname,'wb') as f:
        pickle.dump(results,f)
    return results
#121.520~121.560
#24.998~25.038
#ntu 
lat,lon = 25.018,121.538
#
lat_range = 0.120
lon_range = 0.075
location_map ={}

for lat in numpy.linspace(lat-lat_range,lat+lat_range,(2*lat_range/0.001)+1):
    for lon in numpy.linspace(lon-lon_range,lon+lon_range,(2*lon_range/0.001)+1):
        print(str(lat)+','+str(lon)+' Done')
        results = get_location_result(lat,lon)
        for result in results: 
            location_map[result[0]]=result[1:]
with open('location.txt','rb') as f:
    for location in location_map:
        tmp_str = location.strip()+','+','.join(location_map[location])+'\n'
        f.write(tmp_str)

