import urllib
import urllib2
import cookielib
import re
import csv
import codecs
from bs4 import BeautifulSoup

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'LoginName':'02',
    'Password':'dc20150820if'
})
req = urllib2.Request(    
    url = 'http://gdemba.gicp.net:82/VerifyUser.asp',    
    data = postdata 
)
result = opener.open(req)
for item in cookie:
    print 'Cookie：Name = '+item.name    
    print 'Cookie：Value = '+item.value
result = opener.open('http://gdemba.gicp.net:82/interunit/ListMain.asp?FirstEnter=Yes&Style=0000100003&UID={4C10B953-C0F3-4114-8341-81EF93DE7C55}&TimeID=49252.53')
info = result.read()
soup = BeautifulSoup(info, from_encoding="gb18030")
table = soup.find(id='Table11')
print table

client = ""
tag = ""
tel = ""
catalogue = ""
region = ""
client_type = ""
email = ""
creater = ""
department = ""
action = ""

f = open('table.csv', 'w')
csv_writer = csv.writer(f)
td = re.compile('td')

for row in table.find_all("tr"):
    cells = row.find_all("td")
    if len(cells) == 10:
        client = cells[0].text
        tag = cells[1].text
        tel = cells[2].text
        catalogue = cells[3].text
        region = cells[4].text
        client_type = cells[5].text
        email = cells[6].text
        creater = cells[7].text
        department = cells[8].text
        action = cells[9].text

    csv_writer.writerow([x.encode('utf-8') for x in [client, tag, tel, catalogue, region, client_type, email, creater, department, action]])

f.close()
