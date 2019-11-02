# Control system parameters
def config():
    return {
        # Settings for Arduino Serial Port 
        'port'          : 'COM4',
        'baudrate'      : 9600,
        'timeout'       : 2000,
        # Location of temperature monitoring DLL OpenHardwareMonitor
        'hwm_dir' : 'C:\\Users\\Cooper\\Documents\\Arduino Code\\arduino-pump-control\\hardware_monitor\\OpenHardwareMonitorLib.dll'
    }