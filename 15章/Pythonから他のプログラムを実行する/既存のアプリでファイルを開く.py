import subprocess

with open('hello.txt', 'w', encoding='utf-8') as fw:
    fw.write('Hello world!')

subprocess.Popen(['start', 'hello.txt'], shell=True)
