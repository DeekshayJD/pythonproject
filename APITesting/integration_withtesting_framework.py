import pytest
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

def test_initialize_raid():
    stdout, stderr = run_command("raidcli --initialize")
    assert "Success" in stdout

def test_create_raid5():
    stdout, stderr = run_command("raidcli --create --level 5 --disks /dev/sda /dev/sdb /dev/sdc")
    assert "RAID 5 created" in stdout
