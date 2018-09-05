# pyslink2mseed
Save data for a specific seismic network/station/channel from a seedlink server. This script was originally intended to save network bandwidth of Raspberry Shakes and webservers alike. I used to transfer my data every two minutes via `scp`...now, thankfully, I don't. This script will save a miniSEED file every 50 seconds or so, and datestamped filenames will be created on the fly.

NB: This is NOT a replacement for Earthworm's `ew2mseed` program, which has significantly more built-in failover functionality and does not rely on quite so many heavy libraries to run. It simply is meant to be a placeholder for a larger and harder to set up Earthworm installation.

## Installation and requirements

`pyslink2mseed` requires [`obspy`](https://www.obspy.org/), which requires [Anaconda](https://www.anaconda.com/download). Follow the ObsPy [instructions](https://github.com/obspy/obspy/wiki#installation) for installing via Anaconda, then download and run this script.

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

#### 3. Run the script:
Assuming you have an Anaconda environment named obspy as described in the [obspy docs](https://github.com/obspy/obspy/wiki/Installation-via-Anaconda), you can run (from command line):
```bash
source activate obspy
python pyslink2mseed.py
```

That's basically it. The script will write every minute or so to a miniSEED file that looks like `AM.RCB43.00.SHZ.D.2018.237` where the last two numbers are year in YYYY format and day of year in DDD format. Dates will automatically increment.

On UNIX, you can run this script in the background by specifying, for example:
```bash
python pyslink2mseed.py > /dev/null 2>&1 &
```
which will suppress all output.

I think it's possible to run multiple instances of this script without a problem, but I haven't tested extensively. Let me know what you find.

## Bugs
- Doesn't work with certain versions of `numpy`. File save fails because of integer type error:
```
Exception: Unsupported data type int32 in Stream[0].data
```

## Contact

Questions, comments: ian dot nesbitt at gmail dot com

Bugs, suggestions: [submit an issue](https://github.com/iannesbitt/pyslink2mseed/issues)
