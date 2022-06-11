
import os, shutil, time, subprocess
try:
  subprocess.check_output("pip show pyinstaller")
except subprocess.CalledProcessError:
  os.system("pip install pyinstaller")
print("Drag and drop your py file")
pyPath = input()
print("Drag and Drop your ico file")
ico = input()
os.system(f'pyinstaller "{pyPath}" --icon "{ico}" --onefile')
time.sleep(0.2)
os.remove("main.spec")
shutil.rmtree("build")
print("Succesfully created your exe!")
