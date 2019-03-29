#ver1.0

import os

def ref(reference):
    
    if reference =="identification":
        ref_dir="Database/132_reference_database"
        
    elif reference=="proportion":
        ref_dir="Database/proportion/23_proportion_database"
        
    else:
        print "wrong reference"
        sys.exit('Error: no reference')
        
    return str(ref_dir)


def pipeline(platform,ref_dir):
    
    result =str(raw_input("OUTPUT_FILE name:"))
    
    if platform == "illumina":
        
        fastq_1 = str(raw_input("fastq_1 dir:"))
        fastq_2 = str(raw_input("fastq_2 dir:"))

        systemstr="bowtie2 -p 4 -x "+ref_dir+" -1 "+fastq_1+" -2 "+fastq_2+" | samtools view -bS -> "+result+".bam"
        print systemstr
        os.system(systemstr)

        systemstr="samtools sort -@ 4 "+result+".bam -o "+result+"_sort.bam"
        print systemstr
        os.system(systemstr)

        os.system("rm "+result+".bam")

        systemstr="bedtools genomecov -ibam "+result+"_sort.bam > "+result+".genomecov"
        print systemstr
        os.system(systemstr)

        systemstr="awk -F \'\t\' \'{if($2==0) print $1,1-$5}\' "+result+".genomecov | sort -r -k 2 > "+result+".txt"
        print systemstr
        os.system(systemstr)
        
        
    elif platform =="ion_torrent":
        
        fastq = str(raw_input("fastq dir:"))

        systemstr = "tmap mapall -n 4 -f "+ref_dir+".fa -r "+fastq+" -v -o 1 -s "+result+".sam stage1 map4"
        print systemstr
        os.system(systemstr)

        systemstr="mv "+result+".sam "+result+".bam"
        os.system(systemstr)

        systemstr="samtools sort -@ 4 "+result+".bam -o "+result+"_sort.bam"
        print systemstr
        os.system(systemstr)

        os.system("rm "+result+".bam")

        systemstr="bedtools genomecov -ibam "+result+"_sort.bam > "+result+".genomecov"
        print systemstr
        os.system(systemstr)

        systemstr="awk -F \'\t\' \'{if($2==0) print $1,1-$5}\' "+result+".genomecov | sort -r -k 2 > "+result+".txt"
        print systemstr
        os.system(systemstr)
        
    else:
        print "wrong platform"
        sys.exit('error: worng platform')
            
def main():
    
    reference = str(raw_input("database(identification or proportion):"))
    ref_dir=ref(reference)
    
    platform = str(raw_input("platform(illumina or ion_torrent):"))
    pipeline(platform,ref_dir)

main()
