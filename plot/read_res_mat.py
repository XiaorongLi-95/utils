import json
import os

name = 'muc_25.txt'
task = 25

with open(name, 'r') as f:
    a = f.readlines()
data = {}
for i in range(task):
    b = a[i].split()
    x = []
    for j in range(i+1):
        x.append(float(b[j]))  # *100
    k = 't' + str(i + 1)
    data.update({k: x})

path = os.path.join(name[:-4] + '.json')
with open(path, 'w') as f:
    json.dump(data, f)
