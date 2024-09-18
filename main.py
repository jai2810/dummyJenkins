import os
import subprocess
import sys

if __name__ == '__main__':
    print("Hello world with env variable.")
    status = 1
    with open("env.properties", 'w') as f:
        f.write("POLARIS_BUILD_NUM=J")
    if status!=1:
        sys.exit(0)
    else:
        sys.exit(1)
    

