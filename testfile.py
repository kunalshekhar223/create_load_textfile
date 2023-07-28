import os,re,time
import datetime as datetime

def create_text_file():
    num = 20
    for i in range(1,num+1):
        file_name = f"{i}.txt"
        current_time = datetime.datetime.now()
        content = f"{i}/{current_time}"
        with open(file_name, 'w') as f:
            f.write(content)

def load_text_file():
    current_directory = os.getcwd()
    all_files = os.listdir(current_directory)
    for files in all_files:
        if files.endswith(".txt"):
            with open(files, 'r') as f:
                content = f.read()
                print(content)
                print("\n")

def main():
    start = time.time()
    create_text_file()
    end = time.time()
    runtime = end - start
    print(f"create text file runtime: {runtime:.5f} seconds")
    print("\n")
    start = time.time()
    load_text_file()
    end = time.time()
    runtime = end - start
    print(f"load text file runtime: {runtime:.5f} seconds")


if __name__ == '__main__':
    main()