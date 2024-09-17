import os

if __name__ == '__main__':
    print("Hello world with env variable.")
    shell_command = 'export MY_ENV_VAR=my_value_from_command && env | grep MY_ENV_VAR'

    # Run the shell command and capture the output
    result = subprocess.run(shell_command, capture_output=True, text=True, shell=True, executable='/bin/bash')

    # Check if the command was successful
    if result.returncode == 0:
        # Parse the output to get the environment variable
        output = result.stdout.strip()
        key, value = output.split('=', 1)

        # Set the environment variable in Python
        os.environ[key] = value

        # Verify that the environment variable is set
        print(f"{key} = {os.environ[key]}")
    else:
        print(f"Command failed: {result.stderr}")

