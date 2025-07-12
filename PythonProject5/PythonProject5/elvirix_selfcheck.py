import yaml
import logging

logger = logging.getLogger(__name__)

def load_groups(path="group_list.yaml"):
    try:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        groups = data.get("groups") if isinstance(data, dict) else None
        if not groups:
            logger.warning("group_list.yaml найден, но 'groups' пуст или не там")
            return []
        return groups
    except FileNotFoundError:
        logger.error(f"{path} не найден")
    except Exception as e:
        logger.error(f"Ошибка при парсинге {path}: {e}")
    return []

def check_group_transition(current_group, group_list):
    if not group_list:
        return None
    try:
        nxt = group_list[(group_list.index(current_group) + 1) % len(group_list)]
        return nxt
    except ValueError:
        return group_list[0]

def run():
    groups = load_groups()
    logger.info(f"elvirix_selfcheck: загружено групп — {len(groups)}")