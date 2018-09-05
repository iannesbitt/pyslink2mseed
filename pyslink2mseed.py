from obspy.clients.seedlink.easyseedlink import EasySeedLinkClient
from obspy.core.trace import Trace
from obspy.core.stream import read
from obspy.core import UTCDateTime
import os

# client_addr is in address:port format
client_addr = 'rtserve.iris.washington.edu:18000'
net = 'NE' # network code
sta = 'WES' # station name
loc = '00'
cha = 'HHZ' # channel

day = UTCDateTime.now().strftime('%Y.%j')
i = 1

fn = 'data/%s.%s.%s.%s.D.%s' % (net, sta, loc, cha, day)

if (os.path.isfile(fn)):
	read(fn)


# Subclass the client class
class MyClient(EasySeedLinkClient):
	# Implement the on_data callback
	def on_data(self, trace):
		global i
		global traces
		global fn
		global day
		if i == 1:
			print('Received traces. Checking for existing data...')
			if (os.path.isfile(fn)):
				print('Found %s, reading...' % fn)
				traces = read(fn)
				print('Done.')
			else:
				print('No data found. Creating new blank trace to write to...')
				traces = Trace()
			traces = trace
			print('Trace %s: %s' %(i, trace))
		else:
			print('Trace %s: %s' %(i, trace))
			traces += trace
			traces.__add__(trace)
			if (float(i)/10. == int(float(i)/10.)):
				print('Saving %s traces to %s...' % (i, fn))
				traces.write(fn, format='MSEED')
				print('Done.')
		i += 1
		if (day != UTCDateTime.now().strftime('%Y.%j')):
			day = UTCDateTime.now().strftime('%Y.%j')
			fn = fn = '%s.%s.%s.%s.D.%s' % (net, sta, loc, cha, day)
			i = 1


# Connect to a SeedLink server
client = MyClient(client_addr)

# Retrieve INFO:STREAMS
streams_xml = client.get_info('STREAMS')
print(streams_xml)

# Select a stream and start receiving data
client.select_stream(net, sta, cha)
client.run()
