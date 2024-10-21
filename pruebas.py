from transformers import pipeline

# Cargar el modelo de análisis de sentimientos
analizador_sentimientos = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Analizar un comentario
comentario = "esta bueno el lugar pero le falta sombra y tachos de basura"
resultado = analizador_sentimientos(comentario)
print("El comentario es: ", resultado)
