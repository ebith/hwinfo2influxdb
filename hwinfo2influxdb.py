import sys, time
sys.path.append('lib')

import HWiNFO
from influxdb import InfluxDBClient
import schedule

# Wait for HWiNFO to be launched.
time.sleep(20)

homestats = InfluxDBClient(host='raspberrypi4bserver',database='homestats')
hwinfo = HWiNFO.HwInfoRemote('127.0.0.1')

def job():
  data = hwinfo.get_data()

  # Memory
  for v in data.groups[0].items:
    if v.name == 'Physical Memory Load':
      memory_load = v.value

  # CPU Load
  for v in data.groups[1].items:
    if v.name == 'Total CPU Usage':
      cpu_load = v.value

  # CPU Temp
  for v in data.groups[4].items:
    if v.name == 'CPU Die (average)':
      cpu_temperature = v.value

  # GPU
  for v in data.groups[11].items:
    if v.name == 'GPU Utilization':
      gpu_load = v.value
    if v.name == 'GPU Temperature':
      gpu_temperature = v.value

  points = [
    {
      'measurement': 'desktop',
      'fields': {
        'memory_load': memory_load,
        'cpu_load': cpu_load,
        'cpu_temperature': cpu_temperature,
        'gpu_load': gpu_load,
        'gpu_temperature': gpu_temperature,
      }
    }
  ]
  homestats.write_points(points)

schedule.every(20).seconds.do(job)

while True:
  schedule.run_pending()
  time.sleep(1)
