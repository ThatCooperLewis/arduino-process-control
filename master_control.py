from settings import config as cfg
from hardware_monitor import hardware_monitor
from controllers import serial_control
from utils import pump_utils, numeric_utils


from time import sleep

serial = serial_control.ArduinoSerial()
hwm = hardware_monitor.HardwareMonitor(cfg()['hwm_dir'])
pump = pump_utils.PumpTracking(hwm, serial)
avg = numeric_utils.Averages()

sleep(2)
print('setting default')
serial.write_byte(b'9')

# Main loop
while(True):
    if pump.is_failing(): 
        print('pump failed')
        break
    cpu_load = avg.string_update('cpu_load', hwm.get_cpu_load())
    gpu_temp = avg.string_update('gpu_temp', hwm.get_gpu_temp())
    print('cpu:', round(cpu_load, 2), '\t', 'gpu:', round(gpu_temp, 2), end='\r')



# Do this if main loop breaks
serial.write_byte(b'9')
print("Script closed due to error")



### TODO
'''
build pump speed curve based on average temp
'''
