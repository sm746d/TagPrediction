import json
import os

# list of top ten tags
# already curated from data
top10 = {"javascript": 0, "php": 0, "android": 0, "jquery": 0, "java": 0, "asp.net": 0, "c++": 0, "iphone": 0, "python": 0, "c": 0}

filepath = "../Data/tokenized/"
tokenpath = "../Data/tokenized_data.json"

max_lines = 500
feed = []

def split_by_label(data):
    for row in data:
        for label in top10.keys():
            if (top10[label]<max_lines):
                if label in row["tags"]:
                    feed.append(row)
                    top10[label] = top10[label] + 1
                    break

label_file = open(tokenpath,'w')
for dir, subdir, files in os.walk(filepath):
    for filename in files:
        f = os.path.join(dir,filename)
        if not all(value == max_lines for value in top10.values()):
            file = open(f,'r')
            data = json.load(file)
            split_by_label(data)
        else:
            break

json.dump(feed,label_file)
label_file.close()
file.close()
