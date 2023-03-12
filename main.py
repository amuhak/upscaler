import os
from os import path
import random
import subprocess
from pathlib import Path
import dload
from tkinter import Tk
from tkinter.filedialog import askopenfilename
while(True):
	path1 = os.path.dirname(os.path.realpath(__file__))
	if not (path.exists(path1+"\\realesrgan-ncnn-vulkan-20220424-windows\\realesrgan-ncnn-vulkan.exe")):
		print("Downloding")
		dload.save_unzip( """https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-windows.zip""")
		os.remove(path1+"\\realesrgan-ncnn-vulkan-20220424-windows.zip")		
	model_name="realesrgan-x4plus"
	anime=input("""Is your image anime?
	y/n \n""")
	if anime.lower() in ['y','ye','yes','yess']:
		model_name="realesrgan-x4plus-anime"
	Tk().withdraw()
	input("""Enter input image
New window will open, may not be focused
Press Enter to continue...""")
	in_path = askopenfilename()
	out_path=in_path[0:in_path.rindex("/")]
	name=in_path[in_path.rindex("/")+1:in_path.index('.')]+".png"
	out_path+="/outputs"+"/("+str(random.randint(0,10000))+")"+name
	print(out_path)
	path1+="\\realesrgan-ncnn-vulkan-20220424-windows\\realesrgan-ncnn-vulkan.exe"
	os.system(path1+" -i \""+in_path+"\" -n \""+model_name+"\" -o \""+out_path+"\" -v")

	if not input("Another one? y/n  \n").lower() in ['y','ye','yes','yess']:
		break