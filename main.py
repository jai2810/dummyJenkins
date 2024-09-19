import os
import subprocess
import sys

if __name__ == '__main__':
    subprocess.call("mkdir logs", shell=True)
    build_num=123
    file_with_build_number_as_name = os.environ.get("BUILD_NUMBER")
    path = f"/logs/{file_with_build_number_as_name}"
    with open(path, 'w') as f:
        s = f"{build_num}"
        f.write(s)
    log.info("File written successfully")
    with open(path, 'r') as f:
        log.info("reading file")
        log.info(f.read())
    sys.exit(0)
    

