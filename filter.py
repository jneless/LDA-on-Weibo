import re
pattern1 = re.compile('\d+:.*')
pattern2 = re.compile('\d\d:\d\d')

import os

walk = os.walk('weibo')
r=[]

for root, dirs, files in walk:

    for name in files:

        f = open(os.path.join(root, name), 'r')
        for line in open(os.path.join(root, name), 'r'):

            content=f.readline()
            x=pattern1.findall(content)
            r.extend(x)

rrr=[]
for con in r:
    rr= pattern2.findall(con)

    if len(rr) == 0 and con != []:
        rrr.append(con)


fileObject = open('weibo/output.txt', 'w')
for c in rrr:
    fileObject.write(c)
    fileObject.write('\n')
fileObject.close()