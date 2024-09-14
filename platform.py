import os
import platform
if platform.system() == 'Windows':
    os.system("dir")
elif  platform.system() == 'Linux':
    os.system("ls")
else:
  print("sorry, please check with admain")

