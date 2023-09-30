"""python3 utf_8_encoding.py <filename>"""
import sys


def utf_8_encoding(v: bytes) -> None:
    raw, code_point, remains = "", 0, 0
    for byte in v:
        if (byte & 0b1000_0000) == 0b0000_0000:
            remains = 0
            code_point = byte & 0b0_1111111
            raw = f"{byte:08b}"
        elif (byte & 0b1110_0000) == 0b1100_0000:
            remains = 1
            code_point = byte & 0b000_11111
            raw = f"{byte:08b}"
        elif (byte & 0b1111_0000) == 0b1110_0000:
            remains = 2
            code_point = byte & 0b0000_1111
            raw = f"{byte:08b}"
        elif (byte & 0b1111_1000) == 0b1111_0000:
            remains = 3
            code_point = byte & 0b0000_0111
            raw = f"{byte:08b}"
        elif (byte & 0b1100_0000) == 0b1000_0000:
            remains -= 1
            code_point = (code_point << 6) | (byte & 0b0011_1111)
            raw = raw + f" {byte:08b}"

        if remains == 0:
            print(f"{raw=}, {code_point=:b}, {chr(code_point)}")


def main() -> None:
    filename = sys.argv[1]
    with open(filename, "rb") as f:
        for line in f:
            utf_8_encoding(line)


if __name__ == "__main__":
    main()
