import os
import importlib

# Каталог, где лежат все файлы проекта
project_dir = os.path.dirname(os.path.abspath(__file__))

# Получаем список всех .py файлов, кроме main.py
script_files = [
    f[:-3] for f in os.listdir(project_dir)
    if f.endswith(".py") and f != "main.py"
]

print("🚀 Запускаем модули проекта Elvirix:\n")

for module_name in script_files:
    try:
        print(f"🧩 Модуль: {module_name}")
        module = importlib.import_module(module_name)

        # Если модуль содержит функцию run() — запускаем её
        if hasattr(module, "run") and callable(module.run):
            module.run()
        else:
            print(f"⚠️ Модуль {module_name} не содержит функцию run(), пропущен.")
    except Exception as e:
        print(f"❌ Ошибка при запуске {module_name}: {e}")