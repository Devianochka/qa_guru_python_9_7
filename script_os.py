import os

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
path = os.path.join(CURRENT_DIR, "tmp")
resources = os.path.join(CURRENT_DIR, "resources")
zip_path = os.path.join(resources, "test.zip")