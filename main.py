import os
import pydub

# folder path
src_dir_path = r'C:\Users\D E L L\Desktop\Audio Convertor\argument 1' #Type Here your source file directory
des_dir_path = r'C:\Users\D E L L\Desktop\Audio Convertor\argument 2'  #Type Here your destination file directory

# list to store files
file_names = []
source_paths = []
# Iterate directory
for path in os.listdir(src_dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(src_dir_path, path)) and path.endswith('mp3'):
        file_names.append(path)
        source_paths.append(os.path.join(src_dir_path, path))

for file_name, source_path in zip(file_names, source_paths):
    # To remove extention from fime name
    dot_ind = len(file_name) - file_name.index(".")
    des_file_name = file_name[: - dot_ind]
    #audio convertion process
    sound = pydub.AudioSegment.from_mp3(source_path)
    sound.export(des_dir_path+'\\'+des_file_name+".wav", format="wav")



