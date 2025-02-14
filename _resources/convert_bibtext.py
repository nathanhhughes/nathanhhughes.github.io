#!/usr/bin/env python3
import pathlib

import bibtexparser
import yaml


def _get_multiple(entry, keys):
    for key in keys:
        value = entry.get(key)
        if value is not None:
            return value


def main():
    """Read references and convert to usable site format."""
    bib_file = pathlib.Path(__file__).absolute().parent / "references.bib"
    with bib_file.open("r") as fin:
        library = bibtexparser.parse_string(fin.read())

    references = []
    for entry in library.entries:
        print(entry)
        reference = {}
        try:
            reference["title"] = entry.fields_dict["title"].value
            reference["author"] = entry.fields_dict["author"].value
            reference["year"] = entry.fields_dict["year"].value
            reference["venue"] = _get_multiple(
                entry.fields_dict, ["booktitle", "journal"]
            ).value
        except KeyError as e:
            print(f"Bad entry '{entry}', missing key: {e}")
            continue

        references.append(reference)

    out_file = (
        pathlib.Path(__file__).absolute().parent.parent / "_data" / "references.yaml"
    )

    with out_file.open("w") as fout:
        yaml.dump(references, fout)


if __name__ == "__main__":
    main()
