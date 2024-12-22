# --------------------------------------------------------------------
# Função que constrói o template de prompt para o modelo de geração
# --------------------------------------------------------------------
def create_system_prompt():
    """
    Constrói o prompt com base no contexto do sistema.
        
    Returns:
        str: Prompt para o modelo de geração.
    """
    system_prompt = f""" 
    <task>
        Desenvolva um analisador de texto que processe documentos contendo dados pessoais e extraia informações como RG, CPF e Nome. 
        O programa deve ser capaz de organizar os dados em um arquivo CSV e lidar com possíveis erros no formato ou ausência de informações.
    </task>

    <example>
        Nome,RG,CPF
        João Silva,12.345.678-9,123.456.789-09
        Maria Oliveira,98.765.432-1,987.654.321-00
    </example>

    <instruction>
        1. Leia o conteúdo da imagem fornecida e extraia a informações da imagem.
        2. Use expressões regulares para identificar e extrair as seguintes informações:
            - **Nome**: Dois ou mais nomes próprios, com inicial maiúscula.
            - **RG**: Formato `12.345.678-9` ou `12345678-9`.
            - **CPF**: Formato `000.000.000-00` ou 11 dígitos numéricos.
        3. Estruture os dados extraídos em colunas no arquivo CSV com os cabeçalhos: `Nome`, `RG`, `CPF`.
        4. Valide os dados:
            - Certifique-se de que o CPF possui 11 dígitos válidos.
            - Caso algum campo esteja ausente ou incorreto, registre o erro no arquivo `erros.log`.
    </instruction>
    """
    return system_prompt


def create_user_prompt(user_query):
    """
    Constrói o prompt com base no contexto e na pergunta do usuário.
        
    Returns:
        str: Prompt para o modelo de geração.
    """
    user_prompt = f"""
    <query>
    {user_query}
    </query>
    """
    return user_prompt