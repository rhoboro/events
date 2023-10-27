"""python3 cat.py <filename>"""
import sys


def utf_8_encoding(v: bytes) -> None:
    code_point, remains = 0, 0
    for byte in v:
        if (byte & 0b1000_0000) == 0b0000_0000:
            remains = 0
            code_point = byte & 0b0_1111111
        elif (byte & 0b1110_0000) == 0b1100_0000:
            remains = 1
            code_point = byte & 0b000_11111
        elif (byte & 0b1111_0000) == 0b1110_0000:
            remains = 2
            code_point = byte & 0b0000_1111
        elif (byte & 0b1111_1000) == 0b1111_0000:
            remains = 3
            code_point = byte & 0b0000_0111
        elif (byte & 0b1100_0000) == 0b1000_0000:
            remains -= 1
            code_point = (code_point << 6) | (byte & 0b0011_1111)

        if remains == 0:
            print(f"{chr(code_point)}", end="")


def main() -> None:
    filename = sys.argv[1]
    with open(filename, "rb") as f:
        for line in f:
            utf_8_encoding(line)


if __name__ == "__main__":
    main()
