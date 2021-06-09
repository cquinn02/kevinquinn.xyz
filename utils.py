from os import listdir
from os.path import isfile, join

def get_pics():
    path = "./static/img/"
    filenames = [f for f in listdir(path) if isfile(join(path, f))]
    filenames.sort(reverse=True)

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

    years = [i["date"] for i in info]
    years.sort(reverse=True)
    unique_years = []
    for i in range(len(years)):
        if (i == 0) or (years[i] != years[i - 1]):
            unique_years.append(years[i])

    return info, unique_years