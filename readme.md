# AWS Lambda - Extração de Dados de Imagem usando Bedrock

## 👨‍💻 Projeto desenvolvido por:
[Rafael Torres Nantes](https://github.com/rafael-torres-nantes)

## Índice

* [📚 Contextualização do projeto](#-contextualização-do-projeto)
* [🛠️ Tecnologias/Ferramentas utilizadas](#%EF%B8%8F-tecnologiasferramentas-utilizadas)
* [🖥️ Funcionamento do sistema](#%EF%B8%8F-funcionamento-do-sistema)
* [🔀 Arquitetura da aplicação](#arquitetura-da-aplicação)
* [📁 Estrutura do projeto](#estrutura-do-projeto)
* [📌 Como executar o projeto](#como-executar-o-projeto)
* [🕵️ Dificuldades Encontradas](#%EF%B8%8F-dificuldades-encontradas)

## 📚 Contextualização do projeto

O projeto é focado na **extração de dados de imagens** utilizando o **AWS Bedrock**. Através de técnicas avançadas de machine learning, o sistema é capaz de processar imagens, extrair informações relevantes e organizá-las de forma estruturada. A codificação das imagens em base64 e a integração com o AWS Bedrock são componentes essenciais para garantir a precisão e eficiência na extração dos dados.

### O que é o AWS Bedrock?

O **AWS Bedrock** é um serviço da Amazon Web Services que permite aos desenvolvedores criar, treinar e implantar modelos de machine learning de forma simplificada. Ele oferece uma infraestrutura escalável e ferramentas integradas para facilitar o desenvolvimento de soluções baseadas em inteligência artificial. No contexto deste projeto, o AWS Bedrock é utilizado para processar e analisar documentos, extraindo informações relevantes de maneira automatizada.

### Envio de Imagens para o AWS Bedrock

Para enviar imagens ao AWS Bedrock, é necessário codificá-las em formato base64. A codificação base64 transforma os dados binários da imagem em uma string de texto, permitindo que sejam facilmente transmitidos via HTTP. No projeto, o script `encode_image.py` é responsável por essa tarefa. Após a codificação, a imagem é enviada ao modelo Bedrock, que processa a imagem e retorna os dados extraídos. Esse processo é essencial para garantir que as imagens sejam corretamente interpretadas pelo modelo de machine learning.

O projeto tem como objetivo criar uma solução automatizada para extrair dados de documentos utilizando **AWS Bedrock**. O sistema foi desenhado para processar e analisar documentos, extraindo informações relevantes e organizando-as de forma estruturada.

### Exemplo de Codificação de Imagens

Abaixo está um exemplo de como codificar uma imagem em base64 utilizando Python:

```python
import base64

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

# Exemplo de uso
image_path = 'caminho/para/sua/imagem.jpg'
encoded_image = encode_image_to_base64(image_path)
print(encoded_image)
```

### Envio de Imagem Codificada para o AWS Bedrock

Após codificar a imagem, você pode enviá-la para o AWS Bedrock utilizando a biblioteca `boto3`:

```python
import boto3

def send_image_to_bedrock(encoded_image):
    client = boto3.client('bedrock')
    response = client.invoke_model(
        ModelId='seu-modelo-id',
        Body=encoded_image,
        ContentType='application/json'
    )
    return response

# Exemplo de uso
response = send_image_to_bedrock(encoded_image)
print(response)
```

### Exemplo de Configuração de Credenciais AWS

Para configurar suas credenciais AWS, você pode utilizar o arquivo `.env`:

```
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_REGION=your_aws_region
```

E importar essas variáveis no seu script Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION')
```

## 🛠️ Tecnologias/Ferramentas utilizadas

[<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">](https://www.python.org/)
[<img src="https://img.shields.io/badge/Visual_Studio_Code-007ACC?logo=visual-studio-code&logoColor=white">](https://code.visualstudio.com/)
[<img src="https://img.shields.io/badge/AWS-Bedrock-FF9900?logo=amazonaws&logoColor=white">](https://aws.amazon.com/bedrock/)
[<img src="https://img.shields.io/badge/Boto3-0073BB?logo=amazonaws&logoColor=white">](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
[<img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white">](https://github.com/)

## 🖥️ Funcionamento do sistema

O sistema foi desenvolvido utilizando **Python** e integra-se com **AWS Bedrock** para a extração de dados. A estrutura do projeto inclui scripts para importação de credenciais, verificação de credenciais AWS, formatação de JSON, codificação de imagens e invocação de modelos Bedrock.

## 🔀 Arquitetura da aplicação

O sistema é baseado em uma arquitetura de microserviços, onde o backend se comunica com os serviços da AWS para análise e processamento dos documentos. O AWS Bedrock desempenha um papel central na extração dos dados.

## 📁 Estrutura do projeto

A estrutura do projeto é organizada da seguinte maneira:

```
.
├── utils/
│   ├── import_credentials.py
│   ├── check_aws.py
│   ├── format_json.py
│   ├── encode_image.py
├── bedrock_models/
│   ├── claude_model.py
├── templates/
│   ├── prompts_template.py
├── storage_data/
│   ├── s3_bucket.py
├── lambda_handler.py
├── .env
├── .env.example
├── README.md
```

## 📌 Como executar o projeto

Para executar o projeto localmente, siga as instruções abaixo:

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/rafael-torres-nantes/AWSLambda-ExtractDataUsingBedrock.git
    ```

2. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure as variáveis de ambiente:**
    Preencha o arquivo `.env` com suas credenciais AWS e outras configurações necessárias.

4. **Execute o script principal:**
    ```bash
    python lambda_handler.py
    ```

## 🕵️ Dificuldades Encontradas

Durante o desenvolvimento do projeto, algumas dificuldades foram enfrentadas, como:

- **Integração com serviços AWS:** O uso de credenciais e permissões para acessar o AWS Bedrock exigiu cuidados especiais para garantir a segurança e funcionalidade do sistema.
- **Codificação de imagens:** A implementação da codificação de imagens em base64 para envio ao modelo Bedrock exigiu testes e ajustes para lidar com diferentes formatos e qualidades de arquivos.
- **Aprimoramento do modelo de extração:** O ajuste fino dos prompts e o treinamento de modelos gerativos para obter extrações mais precisas e relevantes foi um desafio contínuo.