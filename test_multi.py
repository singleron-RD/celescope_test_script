"""
Integration tests
"""

import os
import subprocess
from concurrent import futures

import celescope.tools.utils as utils
from celescope.__init__ import RELEASED_ASSAYS

ROOT_PATH = os.path.abspath('.')
LOG_DIR = os.path.join(ROOT_PATH, 'log')

def run_single(assay):
    """
    Returns:
        string indicates complete status
    """
    log_file = os.path.join(LOG_DIR, '{}.log'.format(assay))

    os.chdir(assay)
    print(f"Running {assay}... log file:{log_file}")
    # https://stackoverflow.com/questions/818255/what-does-21-mean
    # cmd 2>&1 >>file does not redirect stderr to the file, but cmd >> file 2>&1 does
    subprocess.check_call(f'sh run_shell.sh > {log_file} 2>&1 ', shell=True)

    with open('sjm.sh', 'w') as sjm_h:
        with open('run_shell.sh', 'r') as shell_h:
            for line in shell_h:
                sjm_h.write(line.replace("mod shell", "mod sjm"))

    subprocess.check_call(f'sh sjm.sh > {log_file} 2>&1', shell=True)
    try:
        subprocess.check_call(f'sh ./shell/test1.sh > {log_file} 2>&1 ', shell=True)
    except subprocess.CalledProcessError:
        return f"{assay} failed"
    return f"{assay} success."


@utils.add_log
def test_mutiple(assays):
    """
    Run all
    >>> pytest -s celescope/tests/test_multi.py 
    Run some tests
    >>> pytest -s celescope/tests/test_multi.py 
    """
    utils.check_mkdir(LOG_DIR)
    print(f'log files are in: {LOG_DIR}')

    if not assays:
        assays = RELEASED_ASSAYS
    else:
        assays = assays.split(',')
    files = os.listdir(".")
    assays = list(set(assays).intersection(set(files)))

    # remove test1
    for assay in assays:
        os.system(f'rm -r {assay}/test1/')
    print("assays to run: ", assays)
    thread = len(assays)
    executor = futures.ProcessPoolExecutor(max_workers=thread)
    results = executor.map(run_single, assays)
    res_list = []
    for result in results:
        res_list.append(result)
    for result in res_list:
        print(result)
    assert not any((string.find("failed") != -1 for string in res_list))
