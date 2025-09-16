from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Mapeamento para as categorias do seu modelo
# Agora, mapeia as etiquetas padrão do modelo para as suas categorias
label_map = {"LABEL_0": "produtivo", "LABEL_1": "improdutivo"}

# Caminho para o diretório onde o modelo foi salvo.
model_path = "utils/fine_tuned_model" 

# Carregue o tokenizador e o modelo fine-tuned
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Crie um pipeline de classificação usando seu modelo local
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)


def classify_email(text):
    # O pipeline retorna um dicionário, e a chave 'label' tem o valor 'LABEL_0' ou 'LABEL_1'
    result = classifier(text)[0]
    
    # Use o mapeamento para traduzir a etiqueta do modelo para sua categoria
    return label_map[result['label']]

def generate_response(classification):
    responses = {
        "produtivo": "Prezado(a), Agradecemos seu contato. Sua solicitação será processada e entraremos em contato o mais breve possível.",
        "improdutivo": "Olá! Agradecemos o contato e desejamos um excelente dia!",
    }
    return responses.get(classification, "Não foi possível sugerir uma resposta.")