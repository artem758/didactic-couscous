import os

DATASETS = {
    "voxforge": "https://repository.voxforge1.org/downloads/VoxForgeCorpus/Trunk/Audio/Main/16kHz_16bit.tar.gz",
    "cremad":   "https://zenodo.org/record/1188976/files/AudioWAV.zip",
    "emodb":    "https://www.phonetik.uni-muenchen.de/Bas/BasEmoDB/emodb.zip",
    "ucf101":   "http://crcv.ucf.edu/data/UCF101/UCF101.rar"
}

def download_dataset(name, url):
    os.makedirs("datasets", exist_ok=True)
    dest = f"datasets/{name}.zip"
    print(f"⬇️ Скачиваем {name}…")
    status = os.system(f"wget --no-check-certificate \"{url}\" -O \"{dest}\"")
    if status != 0:
        print(f"❌ Ошибка загрузки {name} (код {status})")
    else:
        print(f"✅ {name} сохранён в {dest}")

def run():
    print("🚀 Старт загрузки датасетов")
    for name, url in DATASETS.items():
        download_dataset(name, url)
    print("✅ Все датасеты обработаны")