import sys
def clean_file(filename):
    with open(filename,'r') as f:
        lines_token = [line[:-1].split(',') for line in f.readlines()]
        lines_token = [(line[0],line[1:]) for line in lines_token]
        dictionary = dict(lines_token)
    filename = 'clean_'+filename
    with open(filename,'w') as f:
        for key in dictionary:
            tmp_str = key+','+','.join(dictionary[key])+'\n'
            f.write(tmp_str)    

def main(args):
    try:
        src_filename = args[0]
    except:
        raise SystemExit('please input filename')
    clean_file(src_filename)

if __name__ =='__main__': 
    main(sys.argv[1:])