# pyslink2mseed
Save data for a specific seismic network/station/channel from a seedlink server. This script was originally intended to save network bandwidth of Raspberry Shakes and webservers alike. I used to transfer my data every two minutes via `scp`...now, thankfully, I don't. This script will save a miniSEED file every 50 seconds or so, and datestamped filenames will be created on the fly.

## Installation and requirements

`pyslink2mseed` requires `[obspy](https://www.obspy.org/)`, which requires [Anaconda](https://www.anaconda.com/download). Follow the ObsPy [instructions](https://github.com/obspy/obspy/wiki#installation) for installing via Anaconda, then download and run this script.

## Usage
Configuration is pretty straightforward. Just edit the first few lines of the `pyslink2mseed.py` script. If you're looking to find stations to get data from, you should take a look at the [IRIS Station Map](http://geoserver.iris.edu/stations) and the [IRIS Metadata Aggregator](http://ds.iris.edu/mda).

#### 1. Specify the server you'd like to connect to:
To connect to a Raspberry Shake on the local network, change
```python
client_addr = 'rtserve.iris.washington.edu:18000'
```
to, for example,
```python
client_addr = 'raspberryshake.local:18000'
```

#### 2. Choose the stream:
If your Shake's name is RCB43 and it's a short-period instrument (SHZ), your next few lines will be as follows:
```python
net = 'AM' # network code
sta = 'RCB43' # station name
cha = 'SHZ' # channel
```

That's basically it for configuration. The script will write every minute or so to a miniSEED file that looks like `AM.RCB43.00.SHZ.D.2018.237` where the last two numbers are year in YYYY format and day of year in DDD format. Dates will automatically increment.

Questions, comments: ian dot nesbitt at gmail dot com

Bugs, suggestions: [submit an issue](https://github.com/iannesbitt/pyslink2mseed/issues)
