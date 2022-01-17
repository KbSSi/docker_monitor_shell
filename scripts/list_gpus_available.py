import os

ret = os.popen('nvidia-smi')
s = ''
flag = False
use_list = []
for each in ret.readlines():
    s += each

data_part = s.split('|=============================================================================|\n')
# all gpus
def parse(data_part):
    all_list = []
    for each in data_part.split('\n'):
        try:
            all_list.append(int(each[1:7]))
        except:
            pass
    return set(all_list)

all_gpus = parse(data_part[0])
use_gpus = parse(data_part[1])
available_gpus = all_gpus - use_gpus

print('All gpus:',all_gpus)
print('In-process gpus:',use_gpus)
#print('Available gpus:',available_gpus)

