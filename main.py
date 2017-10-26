import subprocess

def get_commits():
    ret = subprocess.check_output(["git", "log"])
    commits = []
    for row in ret.split(b'\n'):
        if row.startswith(b'commit'):
            commits.append(row.split()[1])
    return list(reversed(commits))

def get_diffs(comm1, comm2):
    ret = subprocess.check_output(["git", "diff", comm1, comm2])
    return ret.split(b'\n')


if __name__ == "__main__":
    commits = get_commits()
    if len(commits) < 2:
        print("you don't have enough commits")
    else:
        first_comm, second_comm = commits[0], commits[1]
        print("DIFFS: %s" % get_diffs(first_comm, second_comm))
        for comm in commits[2:]:
            first_comm = second_comm
            second_comm = comm
            print("DIFFS: %s" % get_diffs(first_comm, second_comm))

        
