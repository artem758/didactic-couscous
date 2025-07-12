import os

DATASETS = {
    "voxforge": "https://repository.voxforge1.org/downloads/VoxForgeCorpus/Trunk/Audio/Main/16kHz_16bit.tar.gz",
    "cremad": "https://zenodo.org/record/1188976/files/AudioWAV.zip",
    "emodb": "https://www.phonetik.uni-muenchen.de/Bas/BasEmoDB/emodb.zip",
    "ucf101_sample": "http://crcv.ucf.edu/data/UCF101/UCF101.rar"
}

def download_dataset(name, url):
    os.makedirs("datasets", exist_ok=True)
    path = f"datasets/{name}.zip"
    print(f"⬇️ Скачивание: {name}")
    os.system(f"wget --no-check-certificate \"{url}\" -O \"{path}\"")

def run():
    print("🚀 Запускаем загрузку датасетов...")
    for name, url in DATASETS.items():
        download_dataset(name, url)
    print("✅ Все датасеты успешно загружены")