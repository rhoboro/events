import sys
from dataclasses import dataclass
from pprint import pprint
from struct import unpack
from typing import Self

HEADER_SIZE = 100


@dataclass(frozen=True)
class FileHeader:
    """The Database Header

    https://www.sqlite.org/fileformat2.html#the_database_header
    """

    magic_number: str
    page_size: int
    write_format: int
    read_format: int
    unused_reserved_space: int
    maximum_embedded_payload_fraction: int
    minimum_embedded_payload_fraction: int
    leaf_payload_fraction: int
    file_change_counter: int
    in_header_database_size: int
    first_freelist_trunk_page: int
    freelist_pages: int
    schema_cookie: int
    schema_format_number: int
    default_page_cache_size: int
    largest_root_btree_page: int
    database_text_encoding: int
    user_version: int
    is_incremental_vacuum_mode: int
    application_id: int
    version_valid_for_number: int
    sqlite_version_number: int

    @classmethod
    def parse(cls, filename) -> Self:
        with open(filename, "rb") as f:
            parsed = unpack(">16sHbbbbbbIIIIIIIIIIII20xII", f.read(HEADER_SIZE))
        return FileHeader(*parsed)


def main():
    pprint(FileHeader.parse(sys.argv[1]))


if __name__ == "__main__":
    main()
