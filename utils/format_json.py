import json

def write_jsonl(data, file_path) -> None:
    with open(file_path, "w") as file:
        for item in data:
            json_str = json.dumps(item)
            file.write(json_str + "\n")