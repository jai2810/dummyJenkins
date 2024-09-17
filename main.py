import os
import subprocess

if __name__ == '__main__':
    print("Hello world with env variable.")
    with open("env.properties", 'a') as f:
        f.write("var2=val2")
    

