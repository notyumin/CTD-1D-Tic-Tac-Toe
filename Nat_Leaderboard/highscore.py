import csv
csv_file_path = 'highscore.csv'


def _read_csv(file_path) -> list[dict]:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def get_scores(difficulty):
    data = _read_csv(csv_file_path)
    return list(filter(lambda score: score["difficulty"] == difficulty, data))


def _write_csv(file_path, data):
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "difficulty", "score"])
        writer.writeheader()
        writer.writerows(data)


def update_score(name: str, difficulty: str):
    data = _read_csv(csv_file_path)

    found = False
    for row in data:
        if row["name"] == name and row["difficulty"] == difficulty:
            new_value = int(row["score"]) + 50
            row["score"] = str(new_value)
            found = True

    if not found:
        data.append({"name": name, "difficulty": difficulty, "score": 50})

    data = sorted(data, key=lambda row: float(row["score"]), reverse=True)
    _write_csv(csv_file_path, data)
