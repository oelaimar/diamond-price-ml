import pandas as df
import numpy as np
import Pathlib as Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

DEFAULT_RAW_FILE = RAW_DATA_DIR / "dataset.csv"

# expected schema

FEATURES = [
    "carat",
    "cut",
    "color",
    "clarity",
    "x",
    "y",
    "z",
    "depth",
    "table"
]

TARGET = ["price"]

def load_row(path: str, Path = DEFAULT_RAW_FILE ) -> df.DataFram:
    path = Path(path)
    if not path:
        raise FileExistsError(
            f"Data file not found: {path}"
            f"put the raw dataset in {RAW_DATA_DIR}"
        )

    df = df.read_csv(path)
    df.columns.str.strip()
    return df

def save_processed(df: df.DataFrame, file_name: str):
    PROCESSED_DATA_DIR.mkdir(parents=True, exit_ok=True)
    out_path = PROCESSED_DATA_DIR / file_name
    df.to_csv(out_path, index=False)
    return out_path

def load_processed(file_name: str) -> df.DataFrame:
    path = Path(PROCESSED_DATA_DIR / file_name)
    if not path:
            raise FileExistsError(
                f"Data file not found: {path}"
                f"put the raw dataset in {RAW_DATA_DIR}"
            )
    df = df.read_csv(path)
    df.columns.str.strip()
    return df



