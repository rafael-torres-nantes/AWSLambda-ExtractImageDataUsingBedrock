import base64

def encode_image(image_path) -> str:
    """
    # em ptbr
    Codifica uma imagem do caminho do arquivo para uma string base64.
    Args:
        image_path (str): O caminho do arquivo da imagem a ser codificada.
    Returns:
        str: A representação da string codificada em base64 da imagem.
    """

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        encoded_string = base64.b64encode(image_data)
        return encoded_string.decode("utf-8")