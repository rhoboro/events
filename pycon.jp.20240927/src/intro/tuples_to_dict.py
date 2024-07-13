def tuples_to_dict(
    tuples: list[tuple[str, int]],
) -> dict[str, int] | None:
    if not tuples:
        return None
    return {t[0]: t[1] for t in tuples}


def main():
    ts = [("ham", 1), ("egg", 2)]
    # {'ham': 1, 'egg': 2}
    print(tuples_to_dict(ts))


if __name__ == "__main__":
    main()
