import pandas as pd


exclude_words = [
    "Unit-тестування",
    "Responsibility",
    "Communicability",
    "Knowledge of OOP principles",
    "Discipline",
    "nan",
    "Pydantic",
    "Programming",
    "Backend-розробка",
    "Troubleshooting",
    "Frontend-розробка"
]


def is_english_alphabet(symbol):
    code_point = ord(symbol)
    return (65 <= code_point <= 90) or (97 <= code_point <= 122)


def count_technologies(tech_word_list, keywords):
    tech_count = {keyword: 0 for keyword in keywords}
    word_count = []

    if tech_word_list:
        for word in tech_word_list:
            if word in tech_count and word not in word_count:
                tech_count[word] = 1
                word_count.append(word)

    return tech_count


def data_cleaning():
    df = pd.read_csv("./jobs.csv")

    python_tech_keywords = []

    final_python_tech_keywords = []

    for description in df["description"]:
        python_tech_keywords += str(description).split(",")

    python_tech_keywords = list(set(python_tech_keywords))

    for word in python_tech_keywords:
        if is_english_alphabet(word[0]) and word not in exclude_words:
            final_python_tech_keywords.append(word)

    total_tech_count = {keyword: 0 for keyword in final_python_tech_keywords}

    for description in df["description"]:
        tech_count = count_technologies(str(description).split(","), final_python_tech_keywords)

        for tech, count in tech_count.items():
            total_tech_count[tech] += count

    return total_tech_count
