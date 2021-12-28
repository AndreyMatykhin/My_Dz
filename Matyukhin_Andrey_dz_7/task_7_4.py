import os
from collections import defaultdict
from math import log10

root_dir = "some_data"
stat_dict = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        if size != 0:
            stat_dict[str(10 ** (int(log10(size)) + 1))] += 1
        else:
            stat_dict["10"] += 1

print(sorted(stat_dict.items(), key=lambda x: len(x[0])))
