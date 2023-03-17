import os, sys, venv, time, json


mainDir = os.path.dirname (os.path.abspath (__file__))


def get_path (flag_only: bool = False):
    args = sys.argv [1::]

    if flag_only:
        for arg in args:
            if arg [0] == '-':
                return arg

    else:
        for arg in args:
            if arg [0] != '-':
                return arg


def get_dir_name (dir_path: os.path):
    dir_name = os.path.split (dir_path)

    return dir_name [-1]


def make_venv (path_to_dir: os.path):
    if os.path.exists (path_to_dir):
        print (f"\033[1;31m[-] PathAlreadyExistsError: Can't create venv '{path_to_dir}': File already exists.\033[0m")
        exit ()

    else:
        venv.create (path_to_dir, system_site_packages = False)


def check_if_created (path_to_dir: os.path):
    default_sub_dirs_in_venv = ['include', 'lib', 'lib64', 'bin', 'pyvenv.cfg']
    found = {'include': False, 'lib': False, 'lib64': False, 'bin': False, 'pyvenv.cfg': False}

    if os.path.exists (path_to_dir):
        ld = os.listdir (path_to_dir)

    for i in ld:
        if i in default_sub_dirs_in_venv:
            found [i] = True

        else:
            found [i] = False

    if found ['include'] and found ['lib'] and found ['lib64'] and found ['bin'] and found ['pyvenv.cfg']:
        return True
    
    else: return False


def check_if_test (cmd: list, path: os.path):
    if cmd == '-t' or cmd == '-test':
        time.sleep (10)
        os.system (f"rm -r '{path}'")
        print (f"\033[1;31m[+] Removed '{path}' successfully.\033[0m")


def make_cfg (path_to_dir: os.path, cfg_file: os.path = os.path.join (mainDir, "code-workspace.json")):
    vsc_dir_path = os.path.join (path_to_dir, '.vscode')

    with open (cfg_file) as f:
        cfg = dict (json.load (f))

    # modifying the code-workspace file for the new venv

    cfg ["folders"]["path"]                             = path_to_dir
    cfg ["settings"]["terminal.integrated.cwd"]         = path_to_dir
    cfg ["settings"]["python.defaultInterpreterPath"]   = os.path.join (path_to_dir, 'bin', "python3")

    os.mkdir (vsc_dir_path)

    with open (os.path.join (vsc_dir_path, f'{get_dir_name (path_to_dir)}.code-workspace'), 'w') as f:
        json.dump (cfg, f, indent = 4)


def main ():
    path = get_path ()

    make_venv (path)

    if check_if_created (path):
        make_cfg (path)

    print (f'\033[1;32m[+] Venv created successfully.\033[0m')

    check_if_test (get_path (True), path)


if __name__ == "__main__":
    try:
        main ()

    except KeyboardInterrupt:
        print ('\n\033[1;31m[-]Program exeted, KeyboardInterruptError.\033[0m')
