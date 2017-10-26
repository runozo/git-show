import subprocess
ret = subprocess.check_output(["git", "log"])
print("UEEE: %s" % ret)
