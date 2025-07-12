def load_prompt():
    try:
        with open("prompt.txt", "r") as f:
            return f.read()
    except:
        return "Нет промта."

def run():
    print("✅ elvirix_prompt.txt.py: промт загружен")