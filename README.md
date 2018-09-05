# pyslink
Save data for a specific seismic network/station/channel from a seedlink server.

## Usage:
Configuration is pretty straightforward. Just edit the first few lines of the `slink2mseed.py` script.

To connect to a Raspberry Shake on the local network, change
```python
client_addr = 'rtserve.iris.washington.edu:18000'
```
to, for example,
```python
client_addr = 'raspberryshake.local:18000'
```

If your Shake's name is RCB43 and it's a short-period instrument (SHZ), your next few lines will be as follows:
```python
net = 'AM' # network code
sta = 'RCB43' # station name
loc = '00'
cha = 'SHZ' # channel
```

That's basically it for configuration. The script will output every minute or so to a miniseed file that looks like `AM.RCB43.00.SHZ.D.2018.237` where the last two numbers are year in YYYY format and day of year in DDD format. Dates will automatically increment.
