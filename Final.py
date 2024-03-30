from gensim.models import fasttext
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

model = fasttext.load_facebook_vectors('cc.ru.300.bin.gz')
b = True
while b:
    word = input("Введите слово которое хотите проверить: ")
    embedding_word = model[word].reshape(1, -1)
    dictionary = {
        "банан": model["банан"].reshape(1, -1),
        "апельсин": model["апельсин"].reshape(1, -1),
        "виноград": model["виноград"].reshape(1, -1),
        "аптека":model["аптека"].reshape(1,-1),
        "муравей":model["муравей"].reshape(1,-1,),
        "фасад":model["фасад"].reshape(1,-1),
        "огонь":model["огонь"].reshape(1,-1),
        "зайчик":model["зайчик"].reshape(1,-1,),
        "ежеминутно":model["ежеминутно"].reshape(1,-1),
        "винт":model["винт"].reshape(1,-1),
        "Антарктика":model["Антарктика"].reshape(1,-1),
        "процент":model["процент"].reshape(1,-1),
        "слух":model["слух"].reshape(1,-1),
        "судак":model["судак"].reshape(1,-1),
}
    similarities = {}
    for key, value in dictionary.items():
        similarities[key] = cosine_similarity(embedding_word, value)[0][0]
    most_similar_word = max(similarities, key=similarities.get)
    similarity_score = similarities[most_similar_word]
    print(most_similar_word)
    print("чтобы выйти введите exit, чтобы продолжить введите что угодно")
    if input() == exit:
        b = False
