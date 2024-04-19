import os
import shutil

src_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "ori", "images")
dst_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "ai_001_001", "images")
    
count = 0

while(count < 99):
    print(count)
    for folder in os.listdir(src_folder):
        temp = 0
        for index, filename in enumerate(os.listdir(os.path.join(src_folder, folder))):
            if (index / 4) < count:
                continue
            else:
                if temp < 12:
                    src_path = os.path.join(os.path.join(src_folder, folder), filename)
                    dst_path = os.path.join(os.path.join(dst_folder, folder), filename)
                    shutil.copy(src_path, dst_path)
                    temp += 1
                else:
                    break
        count += 3