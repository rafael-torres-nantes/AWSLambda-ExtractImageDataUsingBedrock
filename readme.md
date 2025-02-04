# Projeto de Inferência com AWS Bedrock

## 👨‍💻 Projeto desenvolvido por:
[Rafael Torres Nantes](https://github.com/rafael-torres-nantes)

## Índice

* 📚 Contextualização do projeto
* 🛠️ Tecnologias/Ferramentas utilizadas
* 🖥️ Funcionamento do sistema
   * 🧩 Parte 1 - Backend
* 🔀 Arquitetura da aplicação
* 📁 Estrutura do projeto
* 📌 Como executar o projeto
* 🕵️ Dificuldades Encontradas

## 📚 Contextualização do projeto

O projeto tem como objetivo criar uma solução automatizada para realizar inferências utilizando **AWS Bedrock**. O sistema foi desenhado para processar imagens e gerar respostas baseadas em prompts fornecidos pelo usuário.

## 🛠️ Tecnologias/Ferramentas utilizadas

[<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">](https://www.python.org/)
[<img src="https://img.shields.io/badge/Visual_Studio_Code-007ACC?logo=visual-studio-code&logoColor=white">](https://code.visualstudio.com/)
[<img src="https://img.shields.io/badge/Boto3-0073BB?logo=amazonaws&logoColor=white">](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
[<img src="https://img.shields.io/badge/Dotenv-ECD53F?logo=dotenv&logoColor=white">](https://pypi.org/project/python-dotenv/)

## 🖥️ Funcionamento do sistema

### 🧩 Parte 1 - Backend

O backend da aplicação foi desenvolvido utilizando **Python**. As principais funcionalidades incluem a integração com AWS Bedrock para a geração de respostas baseadas em prompts e a codificação de imagens em base64.

* **Inferência Bedrock**: A classe 

BedrockInference

 contém a lógica para gerar o corpo da requisição e invocar o modelo Bedrock.
* **Serviços AWS**: A classe 

AWS_SERVICES

 gerencia a sessão AWS e verifica as credenciais.
* **Utilitários**: A pasta 

utils

 contém funções para importação de credenciais AWS e codificação de imagens.

## 🔀 Arquitetura da aplicação

O sistema é baseado em uma arquitetura modular, onde o backend se comunica com os serviços da AWS para análise e processamento das imagens. O AWS Bedrock desempenha um papel central na geração das respostas.

## 📁 Estrutura do projeto

A estrutura do projeto é organizada da seguinte maneira:

```
.
├── bedrock_models/
│   └── bedrock_inference.py
├── image/
├── storage_data/
│   └── s3_bucket.py
├── templates/
│   └── prompts_template.py
├── utils/
│   ├── check_aws.py
│   ├── encode_image.py
│   ├── format_json.py
│   └── import_credentials.py
├── lambda_handler.py
├── .env
├── .env.example
├── .gitignore
└── readme.md
```

## 📌 Como executar o projeto

Para executar o projeto localmente, siga as instruções abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente:**
   Copie o arquivo 

.env.example

 para 

.env

 e preencha com suas credenciais AWS.

4. **Execute o script Lambda localmente:**
   ```bash
   python lambda_handler.py
   ```

## 🕵️ Dificuldades Encontradas

Durante o desenvolvimento do projeto, algumas dificuldades foram enfrentadas, como:

- **Integração com serviços AWS:** O uso de credenciais e permissões para acessar o AWS Bedrock exigiu cuidados especiais para garantir a segurança e funcionalidade do sistema.
- **Codificação de imagens:** A implementação da codificação de imagens em base64 exigiu testes e ajustes para lidar com diferentes formatos e tamanhos de arquivos.
- **Aprimoramento dos prompts:** O ajuste fino dos prompts para obter respostas mais precisas e relevantes foi um desafio contínuo.