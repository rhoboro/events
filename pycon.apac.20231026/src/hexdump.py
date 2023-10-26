"""python3 hexdump.py <filename>"""
import sys

WIDTH = 16
SPACER = "   "


def hexdump(filename: str) -> None:
    display_line = []
    with open(filename, "rb") as f:
        for line in f:
            for byte in line:
                display_line.append(byte)
                if len(display_line) % WIDTH == 0:
                    print(" ".join([f"{b:02X}" for b in display_line]), end="")
                    print(SPACER, end="")
                    print((" ".join([chr(b) for b in display_line])).replace("\n", " "))
                    display_line = []
        else:
            print(" ".join([f"{b:02X}" for b in display_line]), end="")
            print(" ".join(["  " for _ in range(WIDTH - len(display_line))]), end=" ")
            print(SPACER, end="")
            print((" ".join([chr(b) for b in display_line])).replace("\n", " "))


def main():
    hexdump(sys.argv[1])


if __name__ == "__main__":
    main()
