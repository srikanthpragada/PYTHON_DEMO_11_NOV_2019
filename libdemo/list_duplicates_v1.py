import os


def last_path(path):
    pos = path.rfind("\\")
    if pos >= 0:
        return path[pos + 1:]
    else:
        return None


def has_string(st, str_list):
    for s in str_list:
        if s in st:
            return True
    else:
        return False


sdir = r"e:\classroom\python\nov11"
exclude_list = [r'\.git', r'\.mypy_cache']
files = []
for dn, dlist, flist in os.walk(sdir):
    # ignore directories that are in exclude list
    if has_string(dn, exclude_list):
        continue

    for f in flist:
        if f in files:
            print(dn + "\\" + f)
        else:
            files.append(f)
