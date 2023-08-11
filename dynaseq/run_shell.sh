multi_dynaseq \
    --mapfile ./case.mapfile \
    --genomeDir /SGRNJ/Public/Database/genome/mus_musculus/ensembl_92 \
    --STAR_param "--outFilterScoreMinOverLread 0.3 --outFilterMatchNminOverLread 0.3 --outSAMattributes MD" \
    --mod shell
