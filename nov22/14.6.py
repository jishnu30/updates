import urllib
zipcode = '02492'
url = 'http://uszip.com/zip/' + zipcode
conn = urllib.urlopen(url)
for line in conn.fp:
 line = line.strip()
 if 'population':
  print line
 if 'longitude' in line:
  print line
 if 'lattitude' in line:
  print line
conn.close()
