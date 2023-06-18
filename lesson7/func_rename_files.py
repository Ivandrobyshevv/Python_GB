from pathlib import Path


def rename_files(
        new_name: str,
        ext_renamed: str,
        count_digit: int,
        saved_range: range = (3, 6),
        new_ext: str | None = None,
        path: str | None = None,
) -> int:
    if new_ext is None:
        ext_new = ext_renamed
    work_path = Path.cwd() if path is None else Path(path)
    count_renamed = 0
    for p in work_path.iterdir():
        if p.is_file() and p.suffix == ext_renamed:
            file_name = f"{p.stem[saved_range[0]:saved_range[1]]}{new_name}{count_renamed:03}{ext_new}"
            p.rename(Path(p.parent, file_name))
            count_renamed += 1
    return count_renamed


if __name__ == "__main__":
    rename_files()