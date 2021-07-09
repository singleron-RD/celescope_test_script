multi_dynaseq \
    --mapfile ./case.mapfile \
    --chemistry scopeV2.2.1  \
    --genomeDir /SGRNJ/Public/Database/genome/mus_musculus/ensembl_92 \
    --allowNoPolyT \
    --allowNoLinker \
    --STAR_param "--outFilterScoreMinOverLread 0.3 --outFilterMatchNminOverLread 0.3 --outSAMattributes MD" \
    --strand /SGRNJ03/randd/liji/01disk/mousedb/gene.strandedness.csv 
