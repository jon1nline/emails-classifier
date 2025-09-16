import pandas as pd
from datasets import Dataset
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)

# 1. Carregar e Preparar o Dataset (como feito acima)
df = pd.read_csv("emails.csv")
label_map = {"produtivo": 0, "improdutivo": 1}
df["label"] = df["label"].map(label_map)
dataset = Dataset.from_pandas(df)

# Separe os dados em treino e teste (opcional, mas recomendado)
# dataset = dataset.train_test_split(test_size=0.2)
# train_dataset = dataset['train']
# eval_dataset = dataset['test']
train_dataset = dataset
eval_dataset = None  # Para este exemplo simples, vamos treinar em todos os dados

# 2. Carregar o Tokenizador e o Modelo Base
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, num_labels=2
)  # 2 categorias


# Tokenizar o Dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)


tokenized_dataset = train_dataset.map(tokenize_function, batched=True)

# 3. Configurar os Argumentos de Treinamento
training_args = TrainingArguments(
    output_dir="./results",  # Onde os resultados e o modelo serão salvos
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    num_train_epochs=3,  # Número de vezes que o modelo irá ver todos os dados
    weight_decay=0.01,
)

# 4. Criar o Trainer e Treinar o Modelo
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
)

trainer.train()

# 5. Salvar o Modelo e o Tokenizador
model.save_pretrained("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")

print(
    "Treinamento concluído. O modelo e o tokenizador foram salvos em './fine_tuned_model'."
)
