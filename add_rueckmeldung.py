#!/usr/bin/env python3
"""Fügt eine Rückmeldung in die erste freie Zeile der CSV-Datei ein."""

from __future__ import annotations

import csv
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent / "testdatei.csv"
HEADER = ("Vorname", "Nachname", "Rueckmeldung")


def needs_header(rows: list[list[str]]) -> bool:
    if not rows:
        return True
    return rows[0] != list(HEADER)


def read_rows(path: Path) -> list[list[str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as file:
        return [row for row in csv.reader(file)]


def write_rows(path: Path, rows: list[list[str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def main() -> None:
    rows = read_rows(FILE_PATH)
    if needs_header(rows):
        rows = [list(HEADER)] + rows
    rows.append(["Lukas", "Hubolt", "Sehr gute Einführung"])
    write_rows(FILE_PATH, rows)


if __name__ == "__main__":
    main()
