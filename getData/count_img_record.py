import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
from itertools import groupby

dirname = 'img_time'
files = listdir('img_time')
for location_file_name in files:
    lines = open(dirname+'/'+location_file_name).readlines()
    tokens = [line[:-1].split(',') for line in lines]
    data = [{'year':token[0],'mon':token[1],'day':token[2],'hour':token[3],'min':token[4],'sec':token[5]} for token in tokens ]
    f = open("%s/%s.total"%(dirname,location_file_name[:-4]),'w')
    for key,group in groupby(data,lambda x:x['year']):
        f.write("%s:%d\n" %(key,len(list(group))))
    f.write(';')
    for key,group in groupby(data,lambda x:x['year']+','+x['mon']):
        f.write("%s:%d\n" %(key,len(list(group))))
    f.close()
"""
# data 
x = [0,5,9,10,15]
y = [0,1,2,3,4]
 
# trick to get the axes
fig,ax = plt.subplots()
 
# make ticks and tick labels
xticks = range(min(x),max(x)+1,3)
xticklabels = ['2000-01-0'+str(n) for n in range(1,len(xticks)+1)]
 
# plot data
ax.plot(x,y)
 
# set ticks and tick labels
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels,rotation=15)
 
# show the figure
plt.show()
"""