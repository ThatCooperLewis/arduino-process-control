import clr #package pythonnet, not clr

# This is based on an answer found here for temperature reading without needing to run an active program outside this script
# https://stackoverflow.com/questions/3262603/accessing-cpu-temperature-in-python

class HardwareMonitor:

    def __init__(self, dll_dir):
        self.handle = self._initialize_openhardwaremonitor(dll_dir)
        self.sensortypes = ['Voltage','Clock','Temperature','Load','Fan','Flow','Control','Level','Factor','Power','Data','SmallData']
        self.system_stats = {
            'cpu': {
                'load': None
            },
            'gpu': {
                'load': None,
                'temp': None
            },
            'ram': {
                'load':None
            }
        }

    def _initialize_openhardwaremonitor(self, dll_dir):
        # Create and import Open Hardware Monitor .dll
        clr.AddReference(dll_dir)
        from OpenHardwareMonitor import Hardware

        handle = Hardware.Computer()
        handle.MainboardEnabled = True
        handle.CPUEnabled = True
        handle.RAMEnabled = True
        handle.GPUEnabled = True
        handle.HDDEnabled = True
        handle.Open()
        return handle

    def _fetch_stats(self):
        for i in self.handle.Hardware:
            i.Update()
            for sensor in i.Sensors:
                self._parse_sensor(sensor)
            for j in i.SubHardware:
                j.Update()
                for subsensor in j.Sensors:
                    self._parse_sensor(subsensor)

    def _parse_sensor(self,sensor):
            if type(sensor).__module__ == 'OpenHardwareMonitor.Hardware':
                if sensor.Name == 'CPU Total':
                    self.system_stats['cpu']['load'] = sensor.Value
                if sensor.Name == 'GPU Core' and self.sensortypes[sensor.SensorType] == 'Temperature':
                    self.system_stats['gpu']['load'] = sensor.Value
                if sensor.Name == 'GPU Core' and self.sensortypes[sensor.SensorType] ==  'Temperature':
                    self.system_stats['gpu']['temp'] = sensor.Value
                if sensor.Name == 'Memory' and sensor.Hardware.Name == 'Generic Memory':
                    self.system_stats['ram']['load'] = sensor.Value
                    
    def get_system_stats(self):
        self._fetch_stats()
        return self.system_stats

    def get_cpu_load(self):
        self._fetch_stats()
        return self.system_stats['cpu']['load']

    def get_gpu_temp(self):
        self._fetch_stats()
        return self.system_stats['gpu']['temp']