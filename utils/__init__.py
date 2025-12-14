from pathlib import Path

def get_input(input_path: str) -> list[str]:
    path = Path(__file__).resolve().parent / input_path
    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
    
def get_input_raw(input_path: str) -> list[str]:
    path = Path(__file__).resolve().parent / input_path
    with path.open("r", encoding="utf-8") as f:
            input = [line for line in f]