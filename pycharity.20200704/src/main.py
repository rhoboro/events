import argparse
import csv

from pyconus import scrape


def to_csv(sessions, output, fields):
    with open(output, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for session in sessions:
            writer.writerow(session)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="pyconus.csv")
    parser.add_argument("--fields", nargs="+")
    args = parser.parse_args()

    sessions = (session.to_dict() for session in scrape())
    to_csv(sessions, args.output, args.fields)


if __name__ == "__main__":
    main()
