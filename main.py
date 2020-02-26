import subprocess
import datetime

def main(services_i_care_about):
    line_to_write = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for service in services_i_care_about:
        status = subprocess.check_output(['systemctl', 'is-active', service])
        line_to_write = line_to_write + ' ' + service + ' ' + status
    return line_to_write

if __name__ == '__main__':
    services_i_care_about = []
    print(main(services_i_care_about))
