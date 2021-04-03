import sys, os, glob
def run_file(file_path: str):
    files = glob.glob(file_path + "*.py")
    os.system(f"python {files[0]}")
def main():
    try:
        year = sys.argv[1]
        day = sys.argv[2]
        if int(day):
            day = "0"+str(day)
        file_path = f"./{year}/{day}/"

        run_file(file_path)
    except:
        raise Exception("Not enough arguments", [x for x in sys.argv])

if __name__ == "__main__":
    main()
