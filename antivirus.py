import hashlib
import os

malware_hash = list(open("hash_key.txt", 'r').read().split("\n"))


def sha256_file(file_name):
    with open(file_name, 'rb') as f:
        bytes = f.read()
        sha256hash = hashlib.sha256(bytes).hexdigest()
        f.close()

    return sha256hash

# Deep scanning for finding


def sha256_folder(folder_path):

    files = []
    dir_list = list()
    for (dir_path, dir_name, file_name) in os.walk(folder_path):
        dir_list += [os.path.join(dir_path, file) for file in file_name]

    for dir in dir_list:
        if sha256_file(dir) != 0:
            files.append(sha256_file(dir) + ":: FILE :: " + dir)
    print(*files, sep="\n")


# Checking for malware or virus in a single file
def file_scanner(file_path):
    file_hash = sha256_file(file_path)
    global malware_hash

    # checking each file
    for hash in malware_hash:
        if hash == file_hash:
            return "Malware"
    return "No Malware"


virus_file_name = []
virus_file_path = []
# Checking for malware of virus in folder


def folder_scanner(folder_path):

    directory_list = list()

    # for deep scanning
    for (dir_path, dir_name, file_name) in os.walk(folder_path):
        directory_list += [os.path.join(dir_path, file) for file in file_name]

    # checking each file
    for dir in directory_list:
        if file_scanner(dir) != 0:
            if file_scanner(dir) != "No Malware":
                virus_file_name.append(
                    "|| Virus : " + file_scanner(dir) + " || File : " + dir)
                virus_file_path.append(dir)
    print(*virus_file_name, sep="\n")