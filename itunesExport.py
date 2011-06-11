#!/usr/bin/python

import re
import sys
import subprocess
import urlparse
import urllib

playlist = sys.argv[1]
targetdir = sys.argv[2]
print 'importing from %s to %s'%(playlist,targetdir)

playlist_file = open(playlist,"r")

loc_re = re.compile('^.*<key>Location</key><string>(.*)</string>.*$')

for line in playlist_file:
		m = loc_re.match(line)
		if(m):
			raw_url = m.group(1)
			url = urlparse.urlparse(raw_url)
			path = url.path
			filepath = urllib.unquote(urllib.url2pathname(path))
			print filepath
			subprocess.call(['cp',filepath,targetdir])
