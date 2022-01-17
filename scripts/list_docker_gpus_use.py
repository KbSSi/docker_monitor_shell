import os
import json
def get_json(id):
    reader = os.popen(r"docker inspect --format='{{json .HostConfig.DeviceRequests}}' "+id)
    _json = reader.readlines()
    data = json.loads(_json[0])
    if data:
        data = data[0]
        if data['DeviceIDs']:
            return len(list(data['DeviceIDs'])), str(data['DeviceIDs'])
        elif data['Count'] == -1:
            return 'ALL', '-'
        else:
            return str(data['Count']), '-'

    else:
        return '-','-'
print('Container ID\tAllocation gpu count\tAllocation gpu IDs\tContainer name')
f = os.popen('docker ps')
flag = False
for each in f.readlines():
    if not flag:
        flag = True
        continue
    id=each[:12]
    name=each.split(' ')[-1][:-1]
    print(id, end='\t')
    count, deviceids = get_json(id)
    print(str(count)+'\t\t\t'+deviceids+'\t\t\t'+name)
