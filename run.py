import sys, os, glob
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g

oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
def run_file(file_path: str):
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
    files = glob.glob(file_path + "*.py")
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g

oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
    os.system(f"python {files[0]}")
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g

oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
def main():
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
    try:
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
        year = sys.argv[1]
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
        day = sys.argv[2]
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
        if int(day):
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
            day = "0"+str(day)
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
        file_path = f"./{year}/{day}/"
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g

oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
        run_file(file_path)
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
    except:
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
        raise Exception("Not enough arguments", [x for x in sys.argv])
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g

oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
if __name__ == "__main__":
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
    main()
oc/advent_of_code/g
oc/advent_of/code/g
oc/advent_of_code/g
