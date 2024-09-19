import os
import subprocess
import sys

if __name__ == '__main__':
    build_num=123
    file_with_build_number_as_name = os.environ.get("BUILD_NUMBER")
    file_with_build_number_as_name += ".json"
    print(file_with_build_number_as_name)
    with open(file_with_build_number_as_name, 'w') as f:
        s = str.format("{\"build_number\":{}}", build_num)
        f.write(s)
    with open(file_with_build_number_as_name, 'r') as f:
        print("reading file")
        print(f.read())
    sys.exit(0)
    

