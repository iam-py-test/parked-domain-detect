import subprocess
v = subprocess.check_output("google-chrome --version",shell=True).decode().split(" ")[2]
subprocess.run("wget -N https://chromedriver.storage.googleapis.com/{}/chromedriver_linux64.zip -P ~/".format(v),shell=True)
