# CeleScope tests

Please note that these test data are only for testing whether the pipeline can run, and the data does not represent the real data quality. 
For testing purposes and the capacity limit of the GitHub repository, each test data contains only a few reads and may be mixed data from multiple libraries, or simulated data.

## 1. Get test data and scripts.
```
mkdir test_dir
cd test_dir
git clone https://github.com/singleron-RD/celescope_test_data.git
git clone https://github.com/singleron-RD/celescope_test_script.git
```
If github is blocked, an alternate repo(gitee) is available.
```
mkdir test_dir
cd test_dir
git clone https://gitee.com/singleron-rd/celescope_test_data.git
git clone https://gitee.com/singleron-rd/celescope_test_script.git

```

## 2. Modify arguments
- `rna` Change `--genomeDir` to the human genomeDir path.

- `dynaseq` Change `--genomeDir` to the mouse genomeDir path.

- `snp` Change `--genomeDir` to the human genomeDir path.

- `capture_virus` celescope_test_data contains the EBV fasta. You can generate a EBV genomeDir by using `mkref.sh` under `celescope_test_data/capture_virus/EBV_genome`. Then change `--virus_genomeDir` to the EBV genomeDir path.

- `bulk_vdj` Change --ref_path to the igblast ref path.


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

