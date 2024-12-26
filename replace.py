
import shutil

# 指定原始檔案和目標檔案名稱
source_file = 'index.md'
target_file = 'Readme.md'

# 使用 shutil.copy2 來複製檔案，並同時保留原始檔案的屬性和時間戳
shutil.copy2(source_file, target_file)

print(f'檔案 {source_file} 已複製為 {target_file}')