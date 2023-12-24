def abs_path_from_project(relative_path: str):
    import data
    from pathlib import Path

    return (
        Path(data.__file__)
        .parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )