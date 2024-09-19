import os
import subprocess
import sys

if __name__ == '__main__':
    print("Hello world with env variable.")
    print(os.environ.get("BUILD_NUMBER"))
    sys.exit(0)
    

