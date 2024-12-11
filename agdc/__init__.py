import os

# Set hardcoded-macros
ROOT_DIR = os.path.dirname(__file__)
REPO_DIR = '/'.join(ROOT_DIR.split('/')[:-1])
CHECKPOINT_DIR = f"{REPO_DIR}/checkpoints"
ASSET_DIR = f"{REPO_DIR}/assets"