import os
import hashlib

def remove_duplicates(dir_path):
    # dictionary to store file hashes and paths
    file_dict = {}

    # iterate through all files in directory
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            # calculate hash of file content
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()

            # if file content hash already exists, remove the file
            if file_hash in file_dict:
                print(f"Removing duplicate file {file_path}")
                os.remove(file_path)
            else:
                file_dict[file_hash] = file_path

if __name__ == '__main__':
    dir_path = '/path/to/directory'
    remove_duplicates(dir_path)