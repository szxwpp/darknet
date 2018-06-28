import os
import shutil

def DelOrCreate(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)

    os.makedirs(dir)