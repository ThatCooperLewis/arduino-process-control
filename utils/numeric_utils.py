def parse_rpm_result(raw_rpm):
    # Scrap newlines, rewrites, decimals, and whitespace
    return raw_rpm\
            .replace('\n','')\
            .replace('\r','\n')\
            .replace('.00','')\
            .strip()

def sum_list(list_to_sum):
    # Return sum of list of numbers (will fail if not int/float)
    sum = 0
    for num in list_to_sum:
        sum += num
    return sum

def try_to_int(str):
    # Attempt to convert to int, return None on failure
    try: return int(str)
    except: return None


class Averages:

    def __init__(self):
        self.averages = {
#            Created in this format when new string is passed
#            AVG holds newest average, HIST holds the poll history
#            'cpu_load' : {'avg':0,'hist':[]},
        }
        return

    def _update(self, sensor, val, cache_length=5000):
        # Add new value to history
        # If the history is full, remove the oldest and return the average
        sensor['hist'].append(val)
        if len(sensor['hist']) > 5000:
            del sensor['hist'][0]
        sensor['avg'] = sum_list(sensor['hist']) / len(sensor['hist'])
        return sensor

    def string_update(self, sensor_str, val):
        # Take a sensor string (first key in self.averages) and add new value to history
        if sensor_str not in self.averages:
            self.averages[sensor_str] = {'avg':0,'hist':[]}
        self.averages[sensor_str] = self._update(self.averages[sensor_str], val)
        return self.averages[sensor_str]['avg']