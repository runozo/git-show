import subprocess

def get_commits():
    ret = subprocess.check_output(["git", "log"])
    commits = []
    for row in ret.split(b'\n'):
        if row.startswith(b'commit'):
            commits.append(row.split()[1])
    return commits

def get_diffs(comm1, comm2):
    ret = subprocess.check_output(["git", "diff", comm1, comm2])
    return ret


if __name__ == "__main__":
    print("UEEE: %s" % get_commits())
