import json
from datetime import date, datetime
from pathlib import Path
from typing import List

import attr
import cattr

converter = cattr.Converter()


@attr.s(auto_attribs=True, frozen=True)
class Row:
    date: str
    areaCode: str
    areaName: str
    newCasesBySpecimenDateRollingRate: float


@attr.s(auto_attribs=True, frozen=True)
class Dataset:
    length: int
    body: List[Row]


def read_dataset(filename: Path) -> Dataset:
    """
    Read the dataset from the filesystem.
    """

    with filename.open() as f:
        data = json.load(f)

    return converter.structure(data, Dataset)


converter.register_structure_hook(
    date, lambda value, _: datetime.strptime(value, "%Y-%m-%d").date()
)
