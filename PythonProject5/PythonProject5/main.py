import os
import importlib

project_dir = os.path.dirname(os.path.abspath(__file__))
script_files = [
    f[:-3] for f in os.listdir(project_dir)
    if f.endswith(".py") and f != "main.py"
]

print("🟢 Запуск Elvirix...\n")

for name in script_files:
    try:
        module = importlib.import_module(name)
        if hasattr(module, "run") and callable(module.run):
            print(f"▶️ Запускаем {name}.run()")
            module.run()
        else:
            print(f"⚠️ Модуль {name} не содержит run(), пропущен.")
    except Exception as e:
        print(f"❌ Ошибка при запуске {name}: {e}")