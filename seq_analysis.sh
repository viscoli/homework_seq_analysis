#!/bin/bash

#качаем файлики
#fastq-dump  --split-3  SRR5007121

#делаем первые отчеты
fastqc -o reports/ data/raw/SRR5007121_1.fastq
fastqc -o reports/ data/raw/SRR5007121_2.fastq

#начало ридов не нравится, делаем кусь первых 10 нуклеотидов
#java -jar ~/Programmes/Trimmomatic-0.39/trimmomatic-0.39.jar PE ~/Documents/SRR5007121_1.fastq ~/Documents/SRR5007121_2.fastq ~/Documents/SRR5007121_1.trim.fastq ~/Documents/SRR5007121_1un.trim.fastq ~/Documents/SRR5007121_2.trim.fastq ~/Documents/SRR5007121_2un.trim.fastq HEADCROP:10

#отчитываемся
fastqc -o reports/ data/interim/SRR5007121_1.trim.fastq
fastqc -o reports/ data/interim/SRR5007121_2.trim.fastq

#сортируем по gc
python3 src/nice_gc.py

#последние отчеты
fastqc -o reports/ data/processed/SRR5007121_1.trim.Seoul_virus.fastq
fastqc -o reports/ data/processed/SRR5007121_1.trim.trash.fastq
fastqc -o reports/ data/processed/SRR5007121_2.trim.Seoul_virus.fastq
fastqc -o reports/ data/processed/SRR5007121_2.trim.trash.fastq
