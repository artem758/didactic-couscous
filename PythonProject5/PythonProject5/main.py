import os
import importlib
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("main")

def discover_modules(path):
    return [
        fname[:-3] for fname in os.listdir(path)
        if fname.endswith(".py") and fname not in ("main.py",)
    ]

if __name__ == "__main__":
    cwd = os.path.dirname(__file__)
    os.chdir(cwd)
    logger.info("main: старт проекта Elvirix")
    modules = discover_modules(cwd)
    for name in modules:
        try:
            mod = importlib.import_module(name)
            if hasattr(mod, "run"):
                logger.info(f"main: запускаю {name}.run()")
                mod.run()
            else:
                logger.warning(f"main: {name} без run(), пропускаю")
        except Exception as e:
            logger.error(f"main: ошибка в {name}: {e}")
    # После загрузки всех модулей запускаем бота, если он есть
    if "bot" in modules:
        import bot
        bot.run()
    else:
        logger.warning("main: модуль bot не найден")