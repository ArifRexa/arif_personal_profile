import os

directory = "project_images/ATS"
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        print(f'"project_images/ATS/{filename}",')