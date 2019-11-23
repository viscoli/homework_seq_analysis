# make gc nice again!

def readFqFile(file):
	sequences = []
	fastq = []
	with open(file) as f:
		while True:
			name = f.readline().rstrip()
			seq = f.readline().rstrip()
			name2 = f.readline().rstrip()
			qual = f.readline().rstrip()
			if len(seq) == 0:
				break

			sequences.append(seq)
			fastq.append(name)
			fastq.append(seq)
			fastq.append(name2)
			fastq.append(qual)

	return fastq, sequences


def nice_gc (fastq, sequences, good_gc1, good_gc2): # избавляется от неугодного gc
									  # для этого смотрим глазами на отчет из fastqc и выбираем то, что не нравится
									  # good_gc1 - нижнее значение нужного gc, good_gc2 - верхнее значение 
	no_trash = []
	trash = []

	for i, seq in zip(list(range(1,len(fastq)+1,4)),sequences):

		gc_cont =((seq.count('G') + seq.count('C'))/len(seq))*100

		if gc_cont < good_gc1 or gc_cont > good_gc2:
			trash.append(fastq[i-1:i+3])
		else:
			no_trash.append(fastq[i-1:i+3])

	return no_trash, trash


def saveResults(no_trash, trash, path_to_no_trash, path_to_trash):

	with open(path_to_no_trash, 'w') as f:
		for q in no_trash:
			for i in q:
				f.write(i + '\n')

	with open(path_to_trash, 'w') as f:
		for q in trash:
			for i in q:
				f.write(i + '\n')



fastq1, seq1= readFqFile('/home/viscoli/Documents/1/data/interim/SRR5007121_1.trim.fastq')
fastq2, seq2= readFqFile('/home/viscoli/Documents/1/data/interim/SRR5007121_2.trim.fastq')


virus1, trash1 = nice_gc(fastq1, seq1, 37, 43)
virus2, trash2 = nice_gc(fastq2, seq2, 37, 43)


path_virus1 = '/home/viscoli/Documents/1/data/processed/SRR5007121_1.trim.Seoul_virus.fastq'
path_trash1 = '/home/viscoli/Documents/1/data/processed/SRR5007121_1.trim.trash.fastq'
path_virus2 = '/home/viscoli/Documents/1/data/processed/SRR5007121_2.trim.Seoul_virus.fastq'
path_trash2 = '/home/viscoli/Documents/1/data/processed/SRR5007121_2.trim.trash.fastq'

saveResults(virus1, trash1, path_virus1, path_trash1)
saveResults(virus2, trash2, path_virus2, path_trash2)