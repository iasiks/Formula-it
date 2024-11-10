
import json

INPUT_FILE = "input.json"

def task() -> float:
    with open(INPUT_FILE) as f:
        json_data = json.load(f)
    return round(sum([iteam['score'] * iteam['weight'] for iteam in json_data]), 3)


print(task())
