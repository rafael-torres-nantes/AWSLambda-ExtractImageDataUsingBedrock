import base64

def encode_image(image_path) -> str:
    """
    Codifica uma imagem em base64. 

    Args:
        image_path (str): Caminho da imagem a ser codificada.

    Returns:
        str: Imagem codificada em base64.
    """

    # Abre o arquivo de imagem em modo de leitura binária
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()                      # Lê os dados da imagem
        encoded_string = base64.b64encode(image_data)       # Codifica a imagem em base64
        return encoded_string.decode("utf-8")