import os
import hashlib

# specify algorithm to use(sha256). -> open -> read -> calculate sum
def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
                
            sha256_hash.update(data)

    return sha256_hash.hexdigest()


# 
def check_integrity(dir_path):

    # check if the provided path exists or not. If not, then print message
    if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
        print(f"The directory '{dir_path}' does not exist.")

        return
    # If exists, goes through all files in the folder, calls: calculate_sha256 and prints the file path and the Hash sum
    for root, dirs, files, in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            calculated_hash = calculate_sha256(file_path)
            print(f"File path: {file_path} \n/home/kali/test_folder/SHA256 Hash: {calculated_hash}")


# When run it prompts for a path and then it scans every file in the provided path.
if __name__ == "__main__":
    dir_to_check = input("Enter the directory path to check Integrity: ")
    check_integrity(dir_to_check)
