import datetime
import os


image_path = os.listdir("/storage/emulated/0/")
# image_path = "/storage/emulated/0/Acode/delcheck.jpg"
for i in image_path:
    creation_time = os.path.getctime(i)
    three_months_ago = datetime.datetime.now() - datetime.timedelta(days=3*30)
    print(creation_time)
    if creation_time > three_months_ago.timestamp():
        print("yes three months older")
        # os.remove(image_path)
