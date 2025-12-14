from dataclasses import dataclass
from functools import cached_property
from itertools import combinations
from tqdm import tqdm


def get_input(input_path: str) -> list[str]:
    with open(input_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

