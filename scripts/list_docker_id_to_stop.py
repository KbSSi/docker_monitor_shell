import sys
import os
stop_id = []
def get_id():
    reader = os.popen(r"docker ps")
    docker_info = ''
    seq = 1
    for each in reader.readlines():
       seq += 1
       if(seq >= 2):
           docker_info += each
    for each in docker_info.split('\n'):
       each_docker = each.split(' ')
       if(each_docker[0] != ''):
           if(each_docker[3] == "ai3d" and each_docker[36] >= '2' and each_docker[37] == "hours"):
               print(each_docker[0])
               #os.popen("docker down ")
               stop_id.append(each_docker[0])
       #print(each_docker[3])
if __name__=='__main__':
    get_id()
