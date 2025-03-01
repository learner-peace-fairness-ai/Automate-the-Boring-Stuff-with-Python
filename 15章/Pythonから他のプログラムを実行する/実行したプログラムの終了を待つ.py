import subprocess

proc = subprocess.Popen(r'C:\Windows\Notepad.exe')

print(proc.poll() == None)

proc.wait()

print(proc.poll())
