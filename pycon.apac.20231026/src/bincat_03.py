"""python3 bincat_03.py <filename>"""
import sys


def bincat(filename: str) -> None:
    with open(filename, "rb") as f:
        for line in f:
            for byte in line:
                print(f"{byte:09_b} ", end="")
        else:
            print()


def main():
    bincat(sys.argv[1])


if __name__ == "__main__":
    main()
