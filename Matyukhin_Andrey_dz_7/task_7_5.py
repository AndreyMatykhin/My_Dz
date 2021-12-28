import os
from math import log10
import json

root_dir = "some_data"
stat_dict = {}
for root, dirs, files in os.walk(root_dir):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        exten = file.rsplit(".", maxsplit=1)[1].lower()
        if size != 0:
            if str(10 ** (int(log10(size)) + 1)) in stat_dict:
                stat_dict[str(10 ** (int(log10(size)) + 1))][0] += 1
                if not stat_dict[str(10 ** (int(log10(size)) + 1))][1].count(exten):
                    stat_dict[str(10 ** (int(log10(size)) + 1))][1].append(exten)
            else:
                stat_dict[str(10 ** (int(log10(size)) + 1))] = [1, [exten]]
        else:
            if "10" in stat_dict:
                stat_dict["10"][0] += 1
                if not stat_dict["10"][1].count(exten):
                    stat_dict["10"][1].append(exten)
            else:
                stat_dict["10"] = [1, [exten]]

print(sorted(stat_dict.items(), key=lambda x: len(x[0])))
with open("".join([root_dir, '_summary.json']), "w", encoding="utf-8") as f:
    json.dump(stat_dict, f)
