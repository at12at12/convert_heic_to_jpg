import pathlib
import glob
# Pillow and pyheif need to be installed(non standard library)
# Pillow と pyheif は標準ライブラリでないのでインストール必要
from PIL import Image
import pyheif

# function to convert heic to jpeg
# heic から JPEG への変換の関数
def heic_jpg(heic_path, jpg_path):
    # read heic file with using pyheif
    heif_file = pyheif.read(heic_path)

    # heic_file data
    data = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
        )
    
    # save with jpeg format
    data.save(str(jpg_path), "JPEG")

# heic file directry setting 
heic_dir = pathlib.Path('./heic_data/') 
if not heic_dir.exists():
    print("    Heic file stored directry is not found.")
    print("    Check the heic stored directry you set.")
    exit()

# jpg file directry setting 
jpg_dir = pathlib.Path('./jpg_data/')
if not jpg_dir.exists():
    print("    Jpg file stored directry you set is no found.")
    print("    If ok to generate jpg file in the current directry, input 'y': ",end="")
    if input() == 'y':
        jpg_dir = pathlib.Path('./')
    else:
        print("    Finish this process. No new jpg file generated")
        exit()

# heic file catch stored below heic directry(=heic_dir)
heic_path = list(heic_dir.glob('./*.HEIC'))
heic_path += list(heic_dir.glob('./*.heic'))

if len(heic_path) == 0:
    print("    No heic file found in the", heic_dir)
    print("    Finish this process. No new jpg file generated")
    exit()

# convert heic to jpeg
for i in heic_path:
    heic_path = "./" + str(i)
    jpg_path = './jpg_data/' + str(i.stem) + '.jpg'
    if pathlib.Path(jpg_path).exists():
        print("   ", jpg_path,"is existed")
        print("    not generate jpg file")
    else:
        heic_jpg(heic_path, jpg_path)
