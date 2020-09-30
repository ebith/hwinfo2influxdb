# hwinfo2influxdb

## Requirements
- HWiNFO (Remote Center => [x] Server Role)
- InfluxDB

## Usage
```sh
pip install -t lib influxdb schedule
wget -P lib https://raw.githubusercontent.com/mkullber/HWiNFO-RTSS/master/HWiNFO.py
python hwinfo2influxdb.py
```

### Add at startup
```sh
powershell startup.ps1
```
