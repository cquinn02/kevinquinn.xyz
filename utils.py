from os import listdir
from os.path import isfile, join

def get_pics():
    path = "./static/img/"
    filenames = [f for f in listdir(path) if isfile(join(path, f))]
    filenames.reverse()

    info = []
    count = 1
    for f in filenames:
        info.append({
            "index": count,
            "date": f[:4],
            "name": f[7:-4],
            "filename": f
        })
        count += 1

    print(info)
    return info