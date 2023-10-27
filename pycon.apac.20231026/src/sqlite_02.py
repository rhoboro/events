import itertools
import sys
from collections.abc import Iterable
from dataclasses import dataclass, field
from enum import Enum, IntEnum, auto
from struct import unpack
from typing import Any, Self, Union

import sqlparse

HEADER_SIZE = 100
SQLITE_SCHEMA_INDEX_TYPE = 0
SQLITE_SCHEMA_INDEX_NAME = 1
SQLITE_SCHEMA_INDEX_TABLE_NAME = 2
SQLITE_SCHEMA_INDEX_ROOT_PAGE = 3
SQLITE_SCHEMA_INDEX_SQL = 4

ValueType = Union[None, bytes, str, int, float]


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
            parsed = unpack(">16sHBBBBBBIIIIIIIIIIII20xII", f.read(HEADER_SIZE))
        return FileHeader(*parsed)


@dataclass()
class SqliteSchema:
    type: str
    name: str
    table_name: str
    root_page: int
    sql: sqlparse.sql.Statement | None
    is_internal: bool = field(init=False)
    columns: list[tuple[sqlparse.sql.Token, list]] = field(init=False)

    def __post_init__(self):
        self.is_internal = self.table_name.startswith("sqlite_")
        self.columns = self._columns()

    def _columns(self) -> list[tuple[sqlparse.sql.Token, list]]:
        columns = []
        if not self.sql:
            return columns

        for token in self.sql.tokens[-1].tokens:
            if type(token) is sqlparse.sql.Parenthesis:
                continue
            if token.is_whitespace:
                continue
            if str(token.ttype) in ("Token.Punctuation",):
                continue
            if type(token) is sqlparse.sql.Identifier:
                columns.append((token, []))
                continue

            elif type(token) is sqlparse.sql.IdentifierList:
                for t in token.tokens:
                    if type(t) is sqlparse.sql.Identifier:
                        if t.value == "autoincrement":
                            # autoincrement is a keyword
                            continue
                        columns.append((t, []))
                        continue

            columns[-1][1].append(token)

        return columns

    def column_by_name(self, name: str) -> tuple[sqlparse.sql.Token, list]:
        for id_, column in self.columns:
            if id_.value == name:
                return id_, column

        raise NotFound(name)

    def column_by_index(self, index: int) -> tuple[sqlparse.sql.Token, list]:
        try:
            return self.columns[index]
        except IndexError:
            raise NotFound(index)

    def index_by_name(self, name: str) -> int:
        for i, (id_, column) in enumerate(self.columns):
            if id_.value == name:
                return i

        raise NotFound(name)

    def primary_key(self) -> tuple[sqlparse.sql.Token, list]:
        for c in self.columns:
            if [t for t in c[1] if t.value.upper() == "PRIMARY"]:
                return c

        raise NotFound()


class BTreeType(IntEnum):
    TableLeafCell = 0x0D
    TableInteriorCell = 0x05
    IndexLeafCell = 0x0A
    IndexInteriorCell = 0x02

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"


@dataclass(frozen=True)
class BTreeHeader:
    type_flag: BTreeType
    first_free_block: int
    num_of_cells: int
    cell_content: int
    num_of_fragmented_free_bytes: int
    right_most_pointer: int | None = None

    @property
    def size(self) -> int:
        return 8 if self.right_most_pointer is None else 12


class SerialTypeCode(Enum):
    null = auto()
    int_8bit = auto()
    int_16bit = auto()
    int_24bit = auto()
    int_32bit = auto()
    int_48bit = auto()
    int_64bit = auto()
    float_64bit = auto()
    int_0 = auto()
    int_1 = auto()
    internal = auto()
    blob = auto()
    string = auto()

    @classmethod
    def get_code_and_size(cls, num: int) -> tuple["SerialTypeCode", int]:
        code_and_size = SerialTypeCodeMap.get(num)
        if code_and_size is not None:
            return code_and_size[0], code_and_size[1]

        if num == 10 or num == 11:
            raise NotImplementedError()

        if num % 2 == 0:
            return SerialTypeCode.blob, (num - 12) // 2
        else:
            return SerialTypeCode.string, (num - 13) // 2

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"


SerialTypeCodeMap = {
    0: (SerialTypeCode.null, 0),
    1: (SerialTypeCode.int_8bit, 1),
    2: (SerialTypeCode.int_16bit, 2),
    3: (SerialTypeCode.int_24bit, 3),
    4: (SerialTypeCode.int_32bit, 4),
    5: (SerialTypeCode.int_48bit, 6),
    6: (SerialTypeCode.int_64bit, 8),
    7: (SerialTypeCode.float_64bit, 8),
    8: (SerialTypeCode.int_0, 0),
    9: (SerialTypeCode.int_1, 0),
}


@dataclass(frozen=True)
class BTreeTableInteriorCell:
    page_num_of_left_child: int
    rowid: int


@dataclass(frozen=True)
class BTreeCellPayload:
    serial_type: SerialTypeCode
    size: int
    raw_value: bytes

    @property
    def value(self) -> ValueType:
        if self.serial_type == SerialTypeCode.null:
            return None
        elif self.serial_type in (
            SerialTypeCode.int_8bit,
            SerialTypeCode.int_16bit,
            SerialTypeCode.int_24bit,
            SerialTypeCode.int_32bit,
            SerialTypeCode.int_48bit,
            SerialTypeCode.int_64bit,
            SerialTypeCode.int_0,
            SerialTypeCode.int_1,
        ):
            return int.from_bytes(self.raw_value, byteorder="big", signed=True)
        elif self.serial_type == SerialTypeCode.float_64bit:
            return unpack(">f", self.raw_value)[0]
        elif self.serial_type == SerialTypeCode.blob:
            return self.raw_value
        elif self.serial_type == SerialTypeCode.string:
            return self.raw_value.decode()

    def cast(self, value: Any) -> ValueType:
        if self.serial_type == SerialTypeCode.null:
            return value
        elif self.serial_type in (
            SerialTypeCode.int_8bit,
            SerialTypeCode.int_16bit,
            SerialTypeCode.int_24bit,
            SerialTypeCode.int_32bit,
            SerialTypeCode.int_48bit,
            SerialTypeCode.int_64bit,
            SerialTypeCode.int_0,
            SerialTypeCode.int_1,
        ):
            return int(value)
        elif self.serial_type == SerialTypeCode.float_64bit:
            return float(value)
        elif self.serial_type == SerialTypeCode.blob:
            return bytes(value)
        elif self.serial_type == SerialTypeCode.string:
            value = str(value)
            if value.startswith("'") and value.endswith("'"):
                return value[1:-1]
            return value


@dataclass(frozen=True)
class BTreeTableLeafCell:
    num_of_bytes_payload: int
    rowid: int
    payload: list[BTreeCellPayload]
    first_overflow_page: int | None


@dataclass(frozen=True)
class BTreeIndexInteriorCell:
    page_num_of_left_child: int
    num_of_bytes_payload: int
    payload: list[BTreeCellPayload]
    first_overflow_page: int | None


@dataclass(frozen=True)
class BTreeIndexLeafCell:
    num_of_bytes_payload: int
    payload: list[BTreeCellPayload]
    first_overflow_page: int | None


BTreeCell = Union[
    BTreeTableInteriorCell,
    BTreeTableLeafCell,
    BTreeIndexInteriorCell,
    BTreeIndexLeafCell,
]


class BTree:
    def __init__(self, page: bytes, page_num: int, reserved_size: int = 0) -> None:
        self.page = page
        self.page_num = page_num
        self.reserved_size = reserved_size
        self.header = self.parse_header(self.page, self.page_num)
        self.cell_pointers = list(
            self.parse_cell_pointers(self.page, self.page_num, self.header)
        )
        self.rows = [
            self.parse_cell(self.page, self.header, cell_position)
            for cell_position in self.cell_pointers
        ]

    def parse_header(self, page: bytes, page_num: int) -> BTreeHeader:
        offset = HEADER_SIZE if page_num == 1 else 0
        type_flag = unpack(">b", page[offset : offset + 1])[0]
        if type_flag in (BTreeType.IndexInteriorCell, BTreeType.TableInteriorCell):
            header_size = 12
            parsed = unpack(">bhhhbI", page[offset : offset + header_size])
        elif type_flag in (BTreeType.IndexLeafCell, BTreeType.TableLeafCell):
            header_size = 8
            parsed = unpack(">bhhhb", page[offset : offset + header_size])
        else:
            raise SQLiteException("invalid format")

        return BTreeHeader(*parsed)

    def parse_cell_pointers(
        self, page: bytes, page_num: int, header: BTreeHeader
    ) -> Iterable[int]:
        offset = HEADER_SIZE if page_num == 1 else 0
        cell_pointers = page[
            offset + header.size : (offset + header.size) + (2 * header.num_of_cells)
        ]
        for cell_pointer in get_chunk(cell_pointers, 2):
            high, low = list(cell_pointer)
            cell_position = high << 8 | low
            yield cell_position

    def parse_cell(
        self, page: bytes, header: BTreeHeader, cell_position: int
    ) -> BTreeCell:
        if header.type_flag == BTreeType.TableLeafCell:
            return self._parse_table_leaf_cell(page, cell_position)
        elif header.type_flag == BTreeType.TableInteriorCell:
            return self._parse_table_interior_cell(page, cell_position)
        elif header.type_flag == BTreeType.IndexLeafCell:
            return self._parse_index_leaf_cell(page, cell_position)
        elif header.type_flag == BTreeType.IndexInteriorCell:
            return self._parse_index_interior_cell(page, cell_position)

        raise NotImplementedError()

    def _parse_table_leaf_cell(
        self, page: bytes, cell_position: int
    ) -> BTreeTableLeafCell:
        bytes_of_payload, consumed_1 = get_a_varint(page[cell_position:])
        rowid, consumed_2 = get_a_varint(page[cell_position + consumed_1 :])
        row = list(
            self._read_payload(
                page[
                    cell_position
                    + consumed_1
                    + consumed_2 : cell_position
                    + consumed_1
                    + consumed_2
                    + bytes_of_payload
                ],
            )
        )
        return BTreeTableLeafCell(
            num_of_bytes_payload=bytes_of_payload,
            rowid=rowid,
            payload=row,
            # TODO:
            first_overflow_page=None,
        )

    def _parse_table_interior_cell(
        self, page: bytes, cell_position: int
    ) -> BTreeTableInteriorCell:
        page_left_child = int.from_bytes(
            page[cell_position : cell_position + 4], byteorder="big", signed=True
        )
        rowid, consumed = get_a_varint(page[cell_position + 4 :])
        return BTreeTableInteriorCell(
            page_num_of_left_child=page_left_child, rowid=rowid
        )

    def _parse_index_leaf_cell(
        self, page: bytes, cell_position: int
    ) -> BTreeIndexLeafCell:
        bytes_of_payload, consumed_1 = get_a_varint(page[cell_position:])
        row = list(
            self._read_payload(
                page[
                    cell_position
                    + consumed_1 : cell_position
                    + consumed_1
                    + bytes_of_payload
                ],
            )
        )
        return BTreeIndexLeafCell(
            num_of_bytes_payload=bytes_of_payload,
            payload=row,
            # TODO
            first_overflow_page=None,
        )

    def _parse_index_interior_cell(
        self, page: bytes, cell_position: int
    ) -> BTreeIndexInteriorCell:
        page_left_child = int.from_bytes(
            page[cell_position : cell_position + 4], byteorder="big", signed=True
        )
        bytes_of_payload, consumed_1 = get_a_varint(page[cell_position:])
        row = list(
            self._read_payload(
                page[
                    cell_position
                    + consumed_1 : cell_position
                    + consumed_1
                    + bytes_of_payload
                ],
            )
        )
        return BTreeIndexInteriorCell(
            page_num_of_left_child=page_left_child,
            num_of_bytes_payload=bytes_of_payload,
            payload=row,
            # TODO
            first_overflow_page=None,
        )

    def _read_payload(self, payload: bytes) -> Iterable[BTreeCellPayload]:
        bytes_of_header, consumed = get_a_varint(payload)
        columns = []
        while consumed < bytes_of_header:
            serial_type, consumed_ = get_a_varint(payload[consumed:])
            columns.append(SerialTypeCode.get_code_and_size(serial_type))
            consumed += consumed_

        cols = []
        column_pos = consumed
        for col_type, size in columns:
            yield BTreeCellPayload(
                serial_type=col_type,
                size=size,
                raw_value=payload[column_pos : column_pos + size],
            )
            column_pos += size

        return cols

    def print_rows(self) -> None:
        for row in self.rows:
            print("| ", end="")
            for col in row.payload:
                # TODO: Use col.rowid only if col is rowid column
                print(col.value or row.rowid, end=" | ")
            print()


class SQLiteException(Exception):
    pass


class NotFound(SQLiteException):
    pass


class Database:
    def __init__(self, database_file: str) -> None:
        self.database_file = database_file
        self.header = FileHeader.parse(self.database_file)
        # Page 1 of a database file is the root page of a table b-tree
        # that holds a special table named "sqlite_schema".
        # https://www.sqlite.org/fileformat.html#storage_of_the_sql_database_schema
        #
        # CREATE TABLE sqlite_schema(
        #   type text,
        #   name text,
        #   tbl_name text,
        #   rootpage integer,
        #   sql text
        # );
        self.sqlite_schema = BTree(self.read_pages(1, 1, self.page_size), 1)
        self._sqlite_schema_rows = {}

    @property
    def page_size(self) -> int:
        return self.header.page_size

    @property
    def num_of_tables(self) -> int:
        return len(self.sqlite_schema.cell_pointers)

    @property
    def sqlite_schema_rows(self) -> dict[str, SqliteSchema]:
        if self._sqlite_schema_rows:
            return self._sqlite_schema_rows

        for row in self.sqlite_schema.rows:
            if row.payload[SQLITE_SCHEMA_INDEX_SQL].value:
                sql = sqlparse.parse(row.payload[SQLITE_SCHEMA_INDEX_SQL].value)[0]
            else:
                sql = None
            self._sqlite_schema_rows[
                row.payload[SQLITE_SCHEMA_INDEX_NAME].value
            ] = SqliteSchema(
                type=row.payload[SQLITE_SCHEMA_INDEX_TYPE].value,
                name=row.payload[SQLITE_SCHEMA_INDEX_NAME].value,
                table_name=row.payload[SQLITE_SCHEMA_INDEX_TABLE_NAME].value,
                root_page=int(row.payload[SQLITE_SCHEMA_INDEX_ROOT_PAGE].value),
                sql=sql,
            )

        return self._sqlite_schema_rows

    @property
    def tables(self) -> dict[str, SqliteSchema]:
        return {
            name: row
            for name, row in self.sqlite_schema_rows.items()
            if row.type == "table" and not row.table_name.startswith("sqlite_")
        }

    def print_schema(self) -> None:
        for row in self.sqlite_schema_rows.values():
            if row.sql:
                print(row.sql, end=";\n")

    def print_rows(self, table_name: str) -> None:
        table = self.tables.get(table_name)
        if not table:
            raise NotFound(table_name)

        from_table = BTree(
            self.read_pages(table.root_page, 1, self.page_size),
            table.root_page,
        )
        from_table.print_rows()

    def read_pages(self, start: int, num: int, page_size: int) -> bytes:
        # 'start' starts at 1
        with open(self.database_file, "rb") as f:
            f.seek(page_size * (start - 1))
            return f.read(page_size * num)


def get_chunk(iterable, n=5):
    for i, item in itertools.groupby(enumerate(iterable), lambda x: x[0] // n):
        yield (x[1] for x in item)


def get_a_varint(byte_list: bytes) -> tuple[int, int]:
    consumed = 0
    value = 0b00000000
    for byte in byte_list:
        consumed += 1
        if consumed >= 9:
            value = value << 8 | byte
            return value, consumed

        value = value << 7 | (byte & 0b01111111)
        has_next = byte >> 7
        if not has_next:
            return value, consumed
    else:
        raise ValueError()


def main():
    database_file_path = sys.argv[1]
    command = sys.argv[2]
    database = Database(database_file_path)

    if command == ".dbinfo":
        print(f"database page size: {database.page_size}")
        print(f"number of tables: {database.num_of_tables}")

    elif command == ".tables":
        print(" ".join(f"{name}" for name, table in database.tables.items()))

    elif command == ".schema":
        database.print_schema()

    elif command == ".print_rows":
        table_name = sys.argv[3]
        database.print_rows(table_name)

    else:
        print("No such command")


if __name__ == "__main__":
    main()
