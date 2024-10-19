def add(lhs: int, rhs: int) -> int:
    return lhs + rhs

def main() -> None:
    x, y = 1, "1"
    print(add(x, x))
    print(add(y, y))
    print(add(x, y))

if __name__ == "__main__":
    main()

