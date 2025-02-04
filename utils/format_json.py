import json

def write_jsonl(data, file_path) -> None:
    """
    Função que escreve uma lista de dicionários em um arquivo JSONL.

    Args:
        data (list): Lista de dicionários a ser escrita.
        file_path (str): Caminho do arquivo a ser escrito.
    """
    with open(file_path, "w") as file:
        for item in data:
            json_str = json.dumps(item)
            file.write(json_str + "\n")