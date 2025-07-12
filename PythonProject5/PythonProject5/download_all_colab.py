import os

DATASETS = {
    "voxforge": "https://example.com/voxforge.zip",
    "cremad": "https://example.com/cremad.zip",
    "emodb": "https://example.com/emodb.zip",
    "ucf101_sample": "https://example.com/ucf101_sample.zip"
}

def download_dataset(name, url):
    os.system(f"wget {url} -O datasets/{name}.zip")

def run():
    print("🚀 Скачиваем датасеты...")
    for name, url in DATASETS.items():
        download_dataset(name, url)
    print("✅ Все датасеты загружены")