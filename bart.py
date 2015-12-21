#!/usr/bin/python

import httplib
import sys

print sys.argv

def print_usage():
  print 'requires station code as an argument\n'

if len(sys.argv) != 2:
  print_usage
  exit(1)

station_code=sys.argv[1]

from StringIO import StringIO
import xml.etree.ElementTree as etree

estimates = []

c = httplib.HTTPConnection('api.bart.gov')
#c.request("GET",'/api/etd.aspx?cmd=etd&orig=civc&dir=n&key=MW9S-E7SL-26DU-VV8V')
c.request("GET",('/api/etd.aspx?cmd=etd&orig=' + station_code +
  '&key=MW9S-E7SL-26DU-VV8V'))

r = c.getresponse()

print r.status, r.reason
rawdata = r.read()
#for lots of XML, uncomment the next line
#print rawdata

print

#structure
# root 
#   uri    
#   date
#   time
#   station
#   etd
#     destination
#     abbreviation
#     estimate
#       minutes
#       length
#       platform
#       direction
#     estimate
#   etd
#   etd
#   message

#
tree = etree.parse(StringIO(rawdata))

root = tree.getroot()

station = root.find('station')
station.name = station.find('name').text
print station.name
print

station.etds = station.findall('etd')

for etd in station.etds:
  #print list(etd)
  print
  for destination in etd.findall('destination'):
    dest_name=destination.text
    print dest_name
    for estimate in etd.findall('estimate'):
      estimates += [ { 'minutes' : estimate.find('minutes').text,
	'cars' : estimate.find('length').text } ]
    print   
  print estimates
  estimates = []

c.close()
