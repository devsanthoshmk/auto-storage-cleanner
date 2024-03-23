import datetime
import os


image_path = "/home/santhosh/Pictures/pallikaranai nadarajan.png"
# image_path = "/storage/emulated/0/Acode/delcheck.jpg"
creation_time = os.path.getctime(image_path)
three_months_ago = datetime.datetime.now() - datetime.timedelta(days=3*30)
if creation_time < three_months_ago.timestamp():
    print("yes")
    os.remove(image_path)
