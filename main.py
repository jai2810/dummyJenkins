import os
import subprocess
import sys

if __name__ == '__main__':
    print("Hello world with env variable.")
    os.environ["POLARIS_BUILD"]="321"
    

