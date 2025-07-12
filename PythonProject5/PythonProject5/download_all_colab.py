import os
import logging

logger = logging.getLogger(__name__)
DATASETS = {
    "voxforge": "https://repository.voxforge1.org/downloads/VoxForgeCorpus/Trunk/Audio/Main/16kHz_16bit.tar.gz",
    "cremad":   "https://zenodo.org/record/1188976/files/AudioWAV.zip",
    "emodb":    "https://www.phonetik.uni-muenchen.de/Bas/BasEmoDB/emodb.zip",
    "ucf101":   "http://crcv.ucf.edu/data/UCF101/UCF101.rar"
}

def download_dataset(name, url):
    os.makedirs("datasets", exist_ok=True)
    dest = f"datasets/{name}.zip"
    logger.info(f"download_all_colab: скачиваю {name}")
    code = os.system(f"wget --no-check-certificate \"{url}\" -O \"{dest}\"")
    if code != 0:
        logger.error(f"Не удалось скачать {name} (код {code})")
    else:
        logger.info(f"{name} загружен в {dest}")

def run():
    for name, url in DATASETS.items():
        download_dataset(name, url)
    logger.info("download_all_colab: все попытки загрузки выполнены")