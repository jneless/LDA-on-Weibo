import urllib2
import re


headers = {
	    cookie = {"Cookie": "_T_WM=218d5ff524daba6c61bb48c32dcfddc8; SCF=AhLFFiIhCnJBpJYhBP_eX7-lrMwwQlxUnKpQTyTIQBToihrkxopU5K5YgxyQEMEzYnC094riqGZxZNq_-1vGLuQ.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhnNy-sRJ6.03zjCeJY7AX95JpX5KzhUgL.Foq0ShB4e02fSKe2dJLoIpjLxKqL1KnLBo-LxKMLBKMLBo5NSKBRSoB0S0nt; MLOGIN=1; H5_INDEX=3; H5_INDEX_TITLE=%E6%98%B5%E7%A7%B0754864378; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3D103103%26luicode%3D20000173%26fid%3D102803_ctg1_8999_-_ctg1_8999_home%26uicode%3D10000011; SUB=_2A253-XIpDeRhGeRM41YS8yzMwzuIHXVVAh5hrDV6PUJbkdANLXb2kW1NU9I7U3WNlUto7Xqo2xS8JofuLcMpJihY; SUHB=0N2kEF1u1zjmvC; SSOLoginState=1526530681"}  # 将your cookie替换成自己的cookie
	}
pattern1 = re.compile('\/u..\d+')
pattern2 = re.compile('\d+')
AllUser = []
PaperNumber=3
for x in range(1,PaperNumber+1):
    url="https://weibo.com/p/1003061669879400/follow?relate=fans&page=" + str(x)

    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    html=pattern1.findall(html)
    html="".join(html)
    html=pattern2.findall(html)
    AllUser.extend(html)

print(set(AllUser))


