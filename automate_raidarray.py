import subprocess

def configure_raid(level, disks):
    command = f"raidcli --create --level {level} --disks {' '.join(disks)}"
    subprocess.run(command, shell=True)

def run_diagnostics():
    command = "raidcli --diagnostics"
    subprocess.run(command, shell=True)

# Example usage
configure_raid(5, ["/dev/sda", "/dev/sdb", "/dev/sdc"])
run_diagnostics()
