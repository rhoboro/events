"""python3 bincat_02.py <filename>"""
import sys


def bincat(filename: str) -> None:
    with open(filename, "rb") as f:
        for line in f:
            for byte in line:
                print(f"{byte:08b} ", end="")
        else:
            print()


if __name__ == "__main__":
    bincat(sys.argv[1])
