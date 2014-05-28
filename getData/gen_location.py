from urllib.parse   import quote
from urllib.request import urlopen
import urllib.request
import os.path
import pickle
import numpy
#121.520~121.560
#24.998~25.038
#ntu lat,lon = 25.018067665,121.538915634
location_map ={}
for lat in numpy.linspace(24.998,25.038,41):
    for lon in numpy.linspace(121.520,121.560):
        if len(location_map) > 10:
            with open('location.txt','a') as f:
                for location in location_map:
                    tmp_str = location+','+','.join(location_map[location])+'\n'
                    f.write(tmp_str)
        location_map ={}
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
        for result in results: 
            location_map[result[0]]=result[1:]


