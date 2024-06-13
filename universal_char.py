'''
import subprocess

# Using universal_newlines (alias text in newer versions)
result = subprocess.run(['echo', 'Hello\nWorld'], capture_output=True, universal_newlines=True)
print(result.stdout)

import subprocess

# Using text=True for newer Python versions (3.7+)
result = subprocess.run(['cmd', '/c', 'echo Hello\nWorld'], capture_output=True, text=True)
print(result.stdout)


'''

import subprocess
def main():
    # Prepare the string you want to print
    message = "Hello\nWorld"

    # Use Python to print the string, simulating the output handling
    print("Simulated command output:")
    print(message)

    # Simulate running an external command that handles text
    result = subprocess.run(['cmd', '/c', f'echo {message}'], capture_output=True, text=True)
    print("\nCommand output:")
    print(result.stdout)


if __name__ == '__main__':
    main()
