import subprocess
import os

def get_active_processes():
    cmd = 'WMIC PROCESS get Caption,Commandline,Processid'
    sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).stdout
    output_string = ''
    for line in sp:
        output_string += str(line)
    return output_string, sp 


def quit_programs(quit_list):
    active, sp = get_active_processes()
    for program in quit_list:
        if program in active:
            if 'firefox' in program: 
                # Don't force quit, so tabs aren't lost
                quit_command = 'taskkill /IM ' + '"' + program + '"'
            else:
                quit_command = 'taskkill /F /IM ' + '"' + program + '"'
            # st rgs hide the command shell output
            subprocess.run(quit_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    sp.close()

def run_programs(run_list):
    active, sp = get_active_processes()
    for program in run_list:
        exe = program.split('\\')[-1]
        if exe not in active:
            os.startfile(program)
    sp.close()