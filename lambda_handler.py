import json
from bedrock_models.bedrock_inference import BedrockInference
from templates.prompts_template import create_system_prompt, create_user_prompt

def lambda_handler(event, context):
    """
    Função Lambda que invoca o modelo Bedrock para responder a uma pergunta do usuário.

    Args:
        event (dict): Dicionário com os dados de entrada da função Lambda.
        context (object): Objeto de contexto da função Lambda.
    """
    # 1- Imprime o evento recebido
    print(f'[DEBUG] Evento recebido: {event}')
    
    # 2 - Inicializa a classe BedrockInference
    bedrock_inference = BedrockInference()
    
    # 3 - Extrai o prompt do evento
    user_query = event.get('user_query', '')
    image_path = event.get('image_path', '')
    print(f'[DEBUG] Pergunta do usuário: {user_query}')

    # 4 - Gera o prompt do sistema e do usuário
    system_prompt = create_system_prompt()
    user_prompt = create_user_prompt(user_query)
    print(f'[DEBUG] Prompt do sistema: {system_prompt}')
      
    # 5 - Invoca o modelo Bedrock com o prompt combinado
    response_text = bedrock_inference.invoke_model(system_prompt, user_prompt, image_path)
    print(f'[DEBUG] Resposta gerada: {response_text}')
    
    # 6 - Retorna a resposta como JSON
    return {
        'statusCode': 200,
        'body': json.dumps({ 'response': response_text})
    }

lambda_handler({'user_query': 'Oque é esse documento?', 'image_path': './image/teste.jpg'}, None)