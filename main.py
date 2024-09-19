import os
import subprocess
import sys

if __name__ == '__main__':
    build_num=123
    file_with_build_number_as_name = os.environ.get("BUILD_NUMBER")
    file_with_build_number_as_name += ".txt"
    with open(file_with_build_number_as_name, 'w') as f:
        s = f"{build_num}"
        f.write(s)
    log.info("File written successfully")
    with open(file_with_build_number_as_name, 'r') as f:
        log.info("reading file")
        log.info(f.read())
    sys.exit(0)
    

