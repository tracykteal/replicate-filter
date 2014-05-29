These scripts were developed to find artifactually replicated
sequences in 454 data, published in CITATION

Copyright 2009 Thomas Schmidt laboratory.
This program is distrubuted under the terms of the GNU General Public License.

The criteria for artificially replicated reads is that the sequences
are similiar to each other, as defined using the CD-HIT sequence
identity cutoff, and that they start at the same position.  This
criteria is used, because for complex communities, the probability of
getting reads for the same sequence that start at the exact same
position in the metagenome is extremely small.


These scripts use the program CD-HIT
(http://www.bioinformatics.org/cd-hit/) to cluster similiar sequences.
The clusters are then analyzed to determine if reads start at the same
position and are therefore considered artificial replicate reads.

---

The script extract_replicates.py can be used at the command line.
This script takes a 454 fasta file as input, determines which reads
are artifactual replicates and outputs a filtered set that only
contains legitimate unique reads and summary files about the sequences
that were filtered out.

This script requires:
 an installation of cd-hit

 included in the distribution:
 batch_replicates_config.py
 fasta.py
 cd_hit_parse.py
 extract-clusters-html.py

---

INSTALLATION

For installation on Linux or Mac:

(1) Unpack the files with 'tar xvf replicate-filter_1.0.tar.gz --gunzip'

(2)  To run the scripts, first install CD-HIT, available from:

http://www.bioinformatics.org/project/filelist.php?group_id=350

The version used for these scripts is cd-hit-2007-0131.tar.gz

It is also included with this distribution in the scripts directory.

Quick guide to installation of CD-HIT:

 - unpack the file with “tar xvf cd-hit-2007-0131.tar.gz --gunzip”
 - change dir by “cd cd-hit”
 - compile the programs by typing “make”
 - cd-hit will be installed in the directory you're in

If this doesn't work more information is available from CD-HIT's very helpful User Guide
http://www.bioinformatics.org/cd-hit/cd-hit-user-guide.pdf

(3) Change the configuration file to show where your installation of cd-hit is

Edit 'batch_replicates_config.py' in the scripts/ directory

Change the cdhit_dir variable to the path where your cd-hit installation is.

e.g. /home/user/replicates/scripts/cd-hit

If you're not sure what the path is, at the command line, go into the
directory where you have installed cd-hit.  Then type 'pwd' The output
of that command is the path of your cd-hit directory.

(4) Go to the directory where you unpacked the replicate-filter files,
and you're set to run the scripts.


TESTING THE INSTALLATION

Included in the distribution is an example file and example output.
The file example_fasta.fa in the 'examples' directory can be used to
test your installation.  If you run extract-replicates as:

./extract_replicates.py ../example/example_fasta.fa 0.9 0 3 output3

you should get the same thing as the files in example/bpmatch3
directory and the top cluster will have 4 sequences in it.

If you run it with bpmatch=0, you should get the same thing as in
example/bpmatch0 directory, and the top cluster will have 5 sequences
in it.


USING THE SCRIPTS

The scripts are in the scripts/ directory

extract_replicates.py takes a FASTA file of 454 data as input, along
with the parameters that you want to use for the filtering.

Usage: 

./extract_replicates.py <input filename> <sequence identity cutoff> <length difference requirement> <initial base pair requirement> <output directory>

The <sequence identity cutoff> is cd-hits global sequence identity
calculated as the number of identical amino acids in the alignment
divided by the full length of the shorter sequence.  A good value to
start with is 0.9.

The <length difference requirement> is the percent of the sequence
that is required to match. 0 is the default and means that there is no
length restrictions.  This allows for reads of variable lengths.  1
will require that all the sequences in a cluster are the same length.

The <initial base pair requirement> is the number of base pairs
required to match at the beginning of each sequence.  A good value to
start with is 3.

The <output directory> is the directory where you want the output
files to go.


OUTPUT FILES

The output files are:

*.cluster_summary
*_unique.fa
*.fasta_clusters
*.cluster_sizes

*.cluster_summary

This file is a summary of the clusters that are found in the data.  It
reports the total number of sequences in the dataset, the number of
unique sequences found and the percent of the reads that are
artifactual replicates.

It also gives information on the reference sequence for each cluster
and the number of sequences in each cluster.  The reference sequence
is the longest sequence in each cluster.

*_unique.fa

This file is a FASTA file of the unique reads for the dataset.  If
reads cluster, the longest sequence from that cluster is selected as
the unique representative sequence.  All artificially replicated
sequences have been filtered out.

This is the file that you would want to use for further analysis of
your dataset.

*.fasta_clusters

This file shows the sequences that have been grouped into each
cluster.  This is useful if you're determining what threshold or
initial base pair requirement to use and want to see how your reads
are clustering.

*.cluster_sizes

This is a file that can be useful for plotting the distribution of
cluster sizes in your dataset.  The output is the cluster size (the
number of sequences in a cluster) and the number of clusters of that
size.






