import json
from bedrock_models.claude_model import BedrockInference
from storage_data.s3_bucket import S3BucketClass
from templates.prompts_template import create_system_prompt, create_user_prompt

def lambda_handler(event, context):
    # Inicializa a classe BedrockInference
    bedrock_inference = BedrockInference()
    
    # Inicializa a classe S3BucketClass
    s3_bucket = S3BucketClass()
    
    # Extrai o prompt do evento
    user_query = event.get('user_query', '')
    image_path = event.get('image_path', '')
    
    # Gera o prompt do sistema e do usuário
    system_prompt = create_system_prompt()
    user_prompt = create_user_prompt(user_query)
    
    # Combina os prompts
    combined_prompt = f"{system_prompt}\n{user_prompt}"
    
    # Invoca o modelo Bedrock com o prompt combinado
    response_text = bedrock_inference.invoke_model(combined_prompt, image_path)
    
    # Define o nome do bucket e do arquivo no S3
    bucket_name = 'your-s3-bucket-name'
    s3_filename = 'response.json'
    
    # Exporta a resposta para o S3
    s3_bucket.export_dynamodb_to_s3([response_text], bucket_name, s3_filename)
    
    # Retorna a resposta como JSON
    return {
        'statusCode': 200,
        'body': json.dumps({
            'response': response_text,
            's3_location': f"s3://{bucket_name}/{s3_filename}"
        })
    }