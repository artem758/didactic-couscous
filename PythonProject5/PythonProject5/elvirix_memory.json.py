def load_memory():
    try:
        with open("memory.json", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "{}"

def run():
    print("✅ elvirix_memory.json.py запущен — проверка памяти")