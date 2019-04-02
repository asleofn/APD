# APD ( Advanced Probiotics species Detection )

This python script is developed for probiotic species detection from metagenomic sample using whole metagenome shotgun sequencing. This method using the read mapping coverage for species detection and representative genome sequence for each species and sub-species were selected based on all pairwise comparison of all available complete genomes for lactic acid generating bacteria.

[__Prerequisites__]

	- python2	(https://www.python.org/)
	- bowtie2	(http://bowtie-bio.sourceforge.net/bowtie2/index.shtml)
	- SAMtools	(http://samtools.sourceforge.net/)
	- bedtools	(https://bedtools.readthedocs.io/en/latest/)
	- TMAP  	(https://github.com/iontorrent/TS/tree/master/Analysis/TMAP) * for Ion Torrent platform
	
	 # Executables of all program have to be added to ystem Path.
	
  
[__Installation__]

1. Download pre-builted index database.
	
	- Identification for Illumina : https://drive.google.com/open?id=1KrAzIApnJVQjNdeYn5NYsuw0_Ib9naxp
	- Identification for Ion Torrent : https://drive.google.com/open?id=1Eg0rbzHjEjyj9myhMeHPFK0V70e_PycV
	- Proportion for Illumina : https://drive.google.com/open?id=1exQu0AWnfcD8k7BOthGbGxERp_3voICj
	- Proportion for Ion Torrent : https://drive.google.com/open?id=1_zETO4W1KScaK4TRxYo8gG1teFzcfoV3
    
2. Extract the database index file.
		
		mkdir Database && mkdir Database/proportion
		
		(for Illumina platform)
		tar -zxvf 132_reference_database_bowtie2_index.tar.gz -C Database
		tar -zxvf 23_proportion_database_bowtie2_index.tar.gz -C Database/proportion
		
		(for Ion Torrent platform)
		tar -zxvf 132_reference_database_TMAP_index.tar.gz -C Database
		tar -zxvf 23_proportion_database_TMAP_index.tar.gz -C Database/proportion



[__Basic Usage__]

	1. Execute the pipeline.
	
		python APD.py
    
  	2. Select analysis. 
		
		"Analysis (identification or proportion):" --> Select type the Analysis. (Example: identification)
    
  	3. Select Sequencing Platform (Current support Illumina, Ion torrent)
		
		"platform(illumina or ion_torrent):" --> Select the platform for the sequencing file.(Example: illumina)
    
  	4. Prefix of the Result file
		
		"OUTPUT_FILE name:" --> Specify the prefix of output file name. (Example: Result_product_A)
    
  	5. Path of rawdata
		
		"fastq_1 dir:" --> Select forward fastq file.(Example: probiotics_product_A_1.fastq)
		"fastq_2 dir:" --> Select reverse fastq file.(Example: probiotics_product_A_2.fastq)



[__Output__]
	
	1.Identification
		
	(example) Result_product_A.txt
	
	52676,Lactobacillus_acidophilus,GCF_000389675.2 	0.998884
	38578,Streptococcus_thermophilus,GCF_900094135.1 	0.976236
	48963,Enterococcus_faecalis,GCF_001886675.1 		0.940688
	54998,Bifidobacterium_bifidum,GCF_000164965.1 		0.940438
	52829,Lactobacillus_helveticus,GCF_000525715.1 		0.935566
	53113,Lactobacillus_paracasei,GCF_001514415.1 		0.809714
	53140,Lactobacillus_reuteri,GCF_001046835.1 		0.804741
	49823,Lactococcus_lactis,GCF_000006865.1 		0.350231
	
	...
	
	Column 1 : Representative genome of LAB
	Column 2 : mapping coverage
	
	* mapping coverage > 0.7137, it is judged to be identified.
	* In the above example, L.lactis is not included in the product (mapping coverage : 0.350231 < 0.7137).
	
	2.Proportion
	
	The proportion can be calculated through the Result_product_A.genomecov file, see published article M&M for details.
