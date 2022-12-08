import os

with open(".data/temp_file.txt", "r+") as tf_f:
    tf_f.truncate(0)
    tf_f.close()

os.remove(".data/temp_file.txt")

print("All correct!")

