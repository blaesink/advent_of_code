#! /usr/bin/env python

import sys, os, glob

class PathNotFoundError(Exception):
    pass


def has_rust_package(file_path: str) -> bool:
    if os.path.exists(file_path + "rust"):
        return True
    return False

def run_file(file_path: str):
    if os.path.exists(file_path):
        os.chdir(file_path)
        file_path = os.getcwd()
        py_files = glob.glob("*.py")
        rust_package_exists: bool = has_rust_package(file_path)

        # Check to see if we can even run anything
        if not py_files:# and not rs_package_exists:
            raise FileNotFoundError(f"File {file_path}/{files[0]} not found")

        if py_files:
            os.system(f"python {py_files[0]}")
            return 0
        # if rust_package_exists:
        #     print("Rust package exists, running it")
        #     os.chdir("rust/")
        #     os.system("cargo run")
    raise PathNotFoundError(f"Path {file_path} does not exist!")

def main():
    this_directory = os.getcwd()
    try:
        year = sys.argv[1]
        day = sys.argv[2]
        if int(day) < 10:
            day = "0"+str(day)
        file_path = f"{year}/{day}/"

        run_file(file_path)

    except FileNotFoundError as e:
        raise e
    except PathNotFoundError as e:
        raise e
    except:
        if len(sys.argv) < 3:
            raise Exception("Not enough arguments", [x for x in sys.argv])

if __name__ == "__main__":
    main()
