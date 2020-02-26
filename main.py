import subprocess
import datetime

def main(services_i_care_about):
    line_to_write = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for service in services_i_care_about:
        try:
            # Get the status of the service
            # Strip newline character from the end of the line
            status = subprocess.check_output(['systemctl', 'is-active', service])[:-1]
        except subprocess.CalledProcessError as e:
            # Strip the newline from end of the line
            status = e.output[:-1]
        except Exception:
            # Log somthing vaguely useful if we do not know whats gone wrong
            status = 'unknown_exception_in_logger'
        finally:
            line_to_write = line_to_write + ' ' + service + ' ' + status
    return line_to_write

if __name__ == '__main__':
    # Put all the services you care about in this list
    services_i_care_about = []
    print main(services_i_care_about)
