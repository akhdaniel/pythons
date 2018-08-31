import httplib
conn = httplib.HTTPConnection("www.google.com")
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1


conn.close()

