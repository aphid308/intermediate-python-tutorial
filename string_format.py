import os



filepath = "/home/ubuntu/"
filename = "ubuntu.iso"

full_path = os.path.join(filepath, filename)

print("The full path to {} is {}".format(filename, full_path))
