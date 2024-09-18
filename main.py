import os
import subprocess

if __name__ == '__main__':
    print("Hello world with env variable.")
    with open("env.properties", 'w') as f:
        f.write("POLARIS_BUILD_NUM=J")
    return s
    

