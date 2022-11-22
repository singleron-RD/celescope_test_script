"""
Integration tests
"""

import os
import subprocess
from concurrent import futures

import celescope.tools.utils as utils

ROOT_PATH = os.path.abspath('.')
LOG_DIR = os.path.join(ROOT_PATH, 'log')

ASSAYS = [
    'rna',
    'vdj',
    'tag',
    'dynaseq',
    'snp',
    'capture_virus',
    'fusion',
    'flv_CR',
    'flv_trust4',
    'sweetseq',
]


def run_single(assay):
    """
    Returns:
        string indicates complete status
    """
    log_file = os.path.join(LOG_DIR, '{}.log'.format(assay))

    os.chdir(assay)
    print("*" * 20 + "running " + assay + "*" * 20)
    subprocess.check_call(f'sh run_shell.sh 2>&1 > {log_file}', shell=True)

    with open('sjm.sh', 'w') as sjm_h:
        with open('run_shell.sh', 'r') as shell_h:
            for line in shell_h:
                sjm_h.write(line.replace("mod shell", "mod sjm"))

    subprocess.check_call(f'sh sjm.sh 2>&1 > {log_file}', shell=True)
    try:
        subprocess.check_call(f'sh ./shell/test1.sh 2>&1 > {log_file}', shell=True)
    except subprocess.CalledProcessError:
        return f"{assay} failed"
    print("*" * 20 + "success " + assay + "*" * 20)
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
        assays = ASSAYS
    else:
        assays = assays.split(',')

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
