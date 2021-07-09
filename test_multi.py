"""
Integration tests
"""

import os
import subprocess
from concurrent import futures

import celescope.tools.utils as utils

ASSAYS = [
    'rna',
    'vdj',
    'tag',
]


def run_single(assay):
    """
    Returns:
        string indicates complete status
    """
    os.chdir(assay)
    print("*" * 20 + "running " + assay + "*" * 20)
    subprocess.check_call('sh run_shell.sh', shell=True)

    with open('sjm.sh', 'w') as sjm_h:
        with open('run_shell.sh', 'r') as shell_h:
            for line in shell_h:
                sjm_h.write(line.replace("mod shell", "mod sjm"))

    subprocess.check_call('sh sjm.sh', shell=True)
    try:
        subprocess.check_call('sh ./shell/test1.sh', shell=True)
    except subprocess.CalledProcessError:
        return f"{assay} failed"
    print("*" * 20 + "success " + assay + "*" * 20)
    return f"{assay} success."


@utils.add_log
def test_mutiple(assays):
    """
    Run all
    >>> pytest -s celescope/tests/test_multi.py --test_dir {some_dir}
    Run some tests
    >>> pytest -s celescope/tests/test_multi.py --test_dir {some_dir} --assays tag,fusion
    """

    if not assays:
        assays = ASSAYS
    else:
        assays = assays.split(',')
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