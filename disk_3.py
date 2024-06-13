
import subprocess
result = subprocess.run(['wmic', 'OS', 'get', 'FreePhysicalMemory,TotalVisibleMemorySize', '/Value'], capture_output=True, text=True)
print(result.stdout)