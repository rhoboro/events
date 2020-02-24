import argparse
import csv

from pyshizuoka import SESSION_FIELDS, scrape

# contentは改行が含まれる文章なのでデフォルトでは除外する
EXCLUDES = ("content",)


def to_csv(output, fields, sessions):
    with open(output, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for session in sessions:
            writer.writerow(session.to_dict())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", "-o", default="shizuoka.csv", help="出力先ファイル名")
    default_fields = [field for field in SESSION_FIELDS if field not in EXCLUDES]
    parser.add_argument(
        "--fields",
        choices=SESSION_FIELDS,
        nargs="+",
        default=default_fields,
        help=f"出力先ファイルに含めるフィールド(default: {' '.join(default_fields)})",
    )

    args = parser.parse_args()
    to_csv(args.output, args.fields, scrape())


if __name__ == "__main__":
    main()
