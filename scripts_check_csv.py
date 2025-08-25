import csv, pathlib

def check_csv(path: pathlib.Path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)  # comma-delimited by default
        header = next(reader, [])
        exp = len(header)
        bad = []
        for i, row in enumerate(reader, start=2):  # line numbers (1=header)
            if len(row) != exp:
                bad.append((i, len(row), row[:3], row[-3:]))  # preview ends
        return header, exp, bad

def main():
    roots = [pathlib.Path("forms"), pathlib.Path("data")]
    files = []
    for r in roots:
        if r.exists():
            files.extend(sorted(r.glob("*.csv")))
    if not files:
        print("No CSVs found under forms/ or data/")
        return
    for path in files:
        header, exp, bad = check_csv(path)
        if bad:
            print(f"\n{path} — expected {exp} fields based on header:")
            print(", ".join(header))
            for line_no, got, start, end in bad[:10]:
                print(f"  Line {line_no}: saw {got} fields (first/last cols preview {start} … {end})")
            if len(bad) > 10:
                print(f"  … and {len(bad)-10} more problematic lines")
    print("\nDone.")

if __name__ == "__main__":
    main()