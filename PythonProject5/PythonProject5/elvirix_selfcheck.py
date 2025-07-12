import yaml

def load_groups():
    try:
        with open("group_list.yaml", "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if isinstance(data, dict) and "groups" in data:
                return data["groups"]
            print("⚠️ Ключ 'groups' не найден в group_list.yaml")
            return []
    except Exception as e:
        print(f"❌ Ошибка при загрузке group_list.yaml: {e}")
        return []

def check_group_transition(current_group, group_list):
    try:
        index = group_list.index(current_group) + 1
        return group_list[index]
    except (ValueError, IndexError):
        return group_list[0] if group_list else "@default_group"

def run():
    groups = load_groups()
    print(f"✅ Загружено {len(groups)} групп для перехода")