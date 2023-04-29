import os, sys


def get_wd () -> os.path:
    try:
        path = sys.argv [1]

    except IndexError:
        path = os.getcwd ()

    return path


def get_last_Q_no (WD: os.path) -> int:
    Qs_done = []

    for item in os.listdir (WD):
        if item [0] == 'Q':
            try:
                Q_no = int (item.removeprefix ('Q'))

            except:
                pass

            Qs_done.append (Q_no)
    try:
        return max (Qs_done)

    except ValueError:
        return 0


def next_Q (WD: os.path, last_Q_no: int):
    nq = f"Q{last_Q_no + 1}"

    os.chdir (WD)
    os.mkdir (nq)

    return os.path.abspath (nq)


def make_coding_env (lqp):
    os.chdir (lqp)

    files_to_keep = [
        'program.c',
        'output'
    ]

    progFile = os.path.join (lqp, files_to_keep [0])
    optFile = os.path.join (lqp, files_to_keep [1])

    sample_code = [
        '#include <stdio.h>\n',
        '\n',
        '\n',
        'void main (){\n',
        '    printf ("Hello World!\\n");\n',
        '}\n'
    ]

    with open (progFile, 'w') as pf:
        pf.writelines (sample_code)

    os.system (f"gcc -o {optFile} {progFile}")
    os.system ("./output")


def main ():
    wd = get_wd ()
    lqn = get_last_Q_no (wd)
    lqp = next_Q (wd, lqn)

    make_coding_env (lqp)


if __name__ == "__main__":
    main ()


# THE END
