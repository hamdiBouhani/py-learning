import os


dir='./test'
for filename in os.listdir(dir):
    if filename.endswith('.txt'):
        old_path = os.path.join(dir,filename)
        new_path = os.path.join(dir,filename.replace('.txt','.bak'))
        os.rename(old_path,new_path)