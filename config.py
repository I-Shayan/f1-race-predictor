from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR/"data"/"raw"
PROCESSED_DATA_DIR = BASE_DIR/"data"/"processed"
CACHE_DIR = BASE_DIR/"cache"
MODELS_DIR = BASE_DIR/"models"
OUTPUTS_DIR = BASE_DIR/"outputs"
DB_PATH = BASE_DIR/"data"/"myf1.db"

YEARS_TO_COLLECT = [2024]
RANDOM_STATE = 42