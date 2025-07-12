import yaml

def load_groups(path="group_list.yaml"):
    """
    Загружает список групп из YAML-файла.
    Возвращает список строк или пустой список при ошибках.
    """
    try:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        groups = data.get("groups", [])
        if not isinstance(groups, list):
            print("⚠️ 'groups' в файле должен быть списком")
            return []
        return groups
    except FileNotFoundError:
        print(f"⚠️ Файл {path} не найден")
        return []
    except Exception as e:
        print(f"❌ Ошибка при загрузке {path}: {e}")
        return []

def check_group_transition(current_group, group_list):
    """
    Возвращает следующую группу из списка. Если список пуст или
    текущая группа не найдена — возвращает текущую.
    """
    if not group_list:
        print("⚠️ Список групп пуст — нет перехода")
        return current_group
    try:
        idx = group_list.index(current_group) + 1
        return group_list[idx % len(group_list)]
    except ValueError:
        # Текущая группа не в списке — возвращаем первую
        return group_list[0]

def run():
    groups = load_groups()
    print(f"✅ Загружено групп: {len(groups)}")