# CeleScope tests

1. Get test data and scripts.
```
mkdir test_dir
cd test_dir
git clone https://github.com/singleron-RD/celescope_test_data.git
git clone https://github.com/singleron-RD/celescope_test_script.git
```

2. Modify arguments
- `celescope_test_script/rna/run_shell.sh` Modify `--genomeDir`

3. Run `pytest`
- Install pytest
```
pip install pytest
```

- Run all tests
```
cd celescope_test_script
python -m pytest -s test_multi.py 
```

- Run some tests
```
cd celescope_test_script
python -m pytest -s test_multi.py --assays tag,vdj
```

