import json
import os
dirs = 'tiny'
task = 25


def txt2json(name, task):
    file_name = os.path.join(dirs, name)
    with open(file_name, 'r') as f:
        a = f.read()

    b = a.split(')')
    x = []
    for i in b:
        try:
            x.append(float(i[-5:]))  # or -5
        except:
            pass

    data = {}
    for i in range(task):
        k = "t" + str(i + 1)
        data.update({k: []})

    for i in range(task):
        k = 't' + str(i + 1)
        ind = i
        for j in range(task - 1, task - 2 - i, -1):
            data[k].append(x[ind])
            ind = ind + j

    path = os.path.join(dirs, name[:-4] + '.json')
    with open(path, 'w') as f:
        json.dump(data, f)


# for files in os.listdir(dirs):
#     txt2json(files,task)
txt2json('EWC.log', task)
txt2json('SI.log', task)
txt2json('MAS.log', task)
