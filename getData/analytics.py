import matplotlib.pyplot as plt
import numpy as np
def read_data(filename='output_location.txt'):
    with open(filename,'r') as f:
        return [line.strip().split(',') for line in f.readlines()]
def sort_by_img_number(data_list):
    return sorted(data_list,key=lambda x:int(x[2]),reverse=True)
def output_sort_result(f,sort_by_img_number_list,max_rank=10):
    f.write('rank : name,img_number\n')
    for i in range(max_rank+1):
        tmp_str = str(i)+' : '+sort_by_img_number_list[i][1]+','+sort_by_img_number_list[i][2]+'\n'
        f.write(tmp_str)
    f.write('\n')
def output_percent_img_number(filename='img_number',sort_by_img_number_list=None):
    x = []
    y = []
    count = '0'
    data_num = len(sort_by_img_number_list)

    for i in range(data_num):
        if count != sort_by_img_number_list[i][2] :
            x.append(((data_num-i)*100.)/data_num)
            y.append(sort_by_img_number_list[i][2])
            count = sort_by_img_number_list[i][2]
    plt.plot(x,y) 
    plt.xlabel("percent") 
    plt.ylabel("img_number") 
    plt.title("percent_img_number")
    filename += '.png' 
    plt.savefig(filename,dpi=300,format="png") 
def output_percent_img_number_range(filename='img_number_range',sort_by_img_number_list=None):
    data_num = len(sort_by_img_number_list)
    item = [int(data[2]) for data in sort_by_img_number_list]
    plt.hist(item)

    plt.show()
def main():
    data_list = read_data()
    sort_by_img_number_list = sort_by_img_number(data_list)
    with open('result_analytics.txt','w') as f:
        output_sort_result(f,sort_by_img_number_list)
    output_percent_img_number(sort_by_img_number_list=sort_by_img_number_list)
    output_percent_img_number_range(sort_by_img_number_list=sort_by_img_number_list)


if __name__ == '__main__':
    main()