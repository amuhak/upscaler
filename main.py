import os
from os import path
import subprocess
from pathlib import Path
import dload
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
path1 = os.path.dirname(os.path.realpath(__file__))
if not (path.exists(path1+"\\realesrgan-ncnn-vulkan-20220424-windows\\realesrgan-ncnn-vulkan.exe")):
	print("Downloding")
	dload.save_unzip( """https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-windows.zip""")
	os.remove(path1+"\\realesrgan-ncnn-vulkan-20220424-windows.zip")		
model_name="realesrgan-x4plus" 			# realesr-animevideov3 | realesrgan-x4plus | realesrgan-x4plus-anime
anime=input("""Is your image anime?
y/n""")
if anime.lower() in ['y','ye','yes','yess']:
    model_name="realesrgan-x4plus-anime"
Tk().withdraw()
input("""Enter input image
Press Enter to continue...""")
in_path = askopenfilename()
out_path=path1[0:path1.rindex("\\")]
out_path+="out.png"
path1+="\\realesrgan-ncnn-vulkan-20220424-windows\\realesrgan-ncnn-vulkan.exe"
os.system(path1+" -i \""+in_path+"\" -n \""+model_name+"\" -o \""+out_path+"\"")
print("DONE")