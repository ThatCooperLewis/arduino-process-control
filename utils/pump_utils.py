# ---- PUMP UTILS ----
# When called in a loop, the PumpTracking class monitors the arduino output (Pump RPM)
# and returns either the RPM or failure status

import utils.numeric_utils as num

class PumpTracking:

    def __init__(self, hwm, serial):
        self.serial = serial
        self.hwm = hwm
        self.fail_rate = 0
       
    def compute_rpm(self):
        parsed_rpm = num.parse_rpm_result(self.serial.read())
        int_rpm = num.try_to_int(parsed_rpm)
        if int_rpm and int_rpm < 9999:
            self.fail_rate = 0
            return int_rpm
        else:
            self.fail_rate += 1
            return None

    def is_failing(self, fail_threshold=100):
        # If copmute_rpm has failed an X number polls in a row, return True
        self.compute_rpm()
        if self.fail_rate >= fail_threshold:
            return True
        else:
            return False