import logging
import subprocess

# Configure logging
logging.basicConfig(filename='raid_test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_raid_status():
    command = "raidcli --status"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# Log the RAID status
status = check_raid_status()
logging.info("RAID Status:\n%s", status)
