from pathlib import Path

def get_input(input_path: str) -> list[str]:
    with input_path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
    
def get_input_raw(input_path: str) -> list[str]:
    with input_path.open("r", encoding="utf-8") as f:
        return [line for line in f]