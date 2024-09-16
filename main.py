import os

if __name__ == '__main__':
    os.environ["ENV_VARIABLE"] = "JP"
    print(os.environ.get("ENV_VARIABLE"))
    print("Hello world with env variable.")

