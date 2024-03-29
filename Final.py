import numpy as np

def levenshtein_distance(s1, s2):
    """
    Функция для вычисления расстояния Левенштейна между двумя строками.
    """
    m, n = len(s1), len(s2)
    dp = np.zeros((m+1, n+1), dtype=int)

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)

    return dp[m][n]

def find_closest_words(word, dictionary):
    """
    Функция для нахождения наиболее близких слов из словаря к опечатанному слову.
    """
    closest_words = []
    min_distance = float('inf')

    for dict_word in dictionary:
        distance = levenshtein_distance(word, dict_word)
        if distance < min_distance:
            closest_words = [dict_word]
            min_distance = distance
        elif distance == min_distance:
            closest_words.append(dict_word)

    return closest_words

# Пример использования:
dictionary = ["apple", "banana", "cat", "dog", "elephant", "frog"]
word = "elephan"

closest_words = find_closest_words(word, dictionary)
print("Опечатанное слово:", word)
print("Наиболее близкие слова в словаре:", closest_words)
