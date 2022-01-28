# CeleScope tests

Please note that these data are for testing purposes only. Some of the data are artificially generated.

## 1. Get test data and scripts.
```
mkdir test_dir
cd test_dir
git clone https://github.com/singleron-RD/celescope_test_data.git
git clone https://github.com/singleron-RD/celescope_test_script.git
```

## 2. Modify arguments
- rna

`celescope_test_script/rna/run_shell.sh` Change `--genomeDir` to the human genomeDir path.

- dynaseq

`celescope_test_script/dynaseq/run_shell.sh` Change `--genomeDir` to the mouse genomeDir path.

- snp

`celescope_test_script/snp/run_shell.sh` Change `--genomeDir` to the human genomeDir path.

- capture_virus

celescope_test_data contains the EBV fasta. You can generate a EBV genomeDir by using `mkref.sh` under `celescope_test_data/capture_virus/EBV_genome` .

`celescope_test_script/capture_virus/run_shell.sh` Change `--virus_genomeDir` to the EBV genomeDir path.


## 3. Run `pytest`
- Install pytest
```
pip install pytest
```

- Run some tests
```
cd celescope_test_script
python -m pytest -s test_multi.py --assays tag,vdj
```

- Run all tests
```
cd celescope_test_script
python -m pytest -s test_multi.py 
```

