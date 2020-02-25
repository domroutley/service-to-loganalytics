import subprocess
import datetime

def main():
    services_i_care_about = []
    line_to_write = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    all_services = subprocess.check_output(['systemctl', '--all'])

    for line in all_services.decode('utf-8').splitlines():
        if len(services_i_care_about) == 0:
            # We have found them all
            break
        for service in services_i_care_about:
            if service in line:
                line_to_write = line_to_write + ';' + ' '.join(line.split())
                # Do not bother looking for this service again
                services_i_care_about.remove(service)
                # Stop looking through the list of services
                break
    print line_to_write

if __name__ == '__main__':
    main()
