These scripts were developed to find artifactually replicated sequences in 454 data, published
in CITATION

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

This program can be run through a web interface or at the command
line.  For information on the command line script, see the README.

These notes README_CGI describe how to set up a web interface for
doing 454 replicate filtering.

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

If this doesn't work more information is available from CD-HIT's very
helpful User Guide
http://www.bioinformatics.org/cd-hit/cd-hit-user-guide.pdf

(3) Change the configuration file to show where your installation of
cd-hit is and where your web directories will be

Edit 'replicates_config.py'

Change the cdhit_dir variable to the path where your cd-hit
installation is.


(4) Change update.sh so that the files from the local directory update
to the correct web directories.  Instead of doing this, you could also
create symbolic links if your operating system allows it.  Or you
could just copy the files and forget about it, but this is a nice
setup if you want to be able to edit the scripts a little more easily.

(5) Run update.sh (or link or copy the files)

(6) Go to the url that you set as 'url' in the replicates_config.py
file.  The site should be there and ready to go.*

* Of course the look and feel of the site is like the Schmidt lab web
site.  If you want to change this, you can edit html/index.html which
controls the look of the front page and
scripts/repeats_html_template.py that controls the look of the page
where the results are returned.




USING THE SCRIPTS

extract_replicates.py takes a FASTA file of 454 data as input, along
with the parameters that you want to use for the filtering.

Usage: 

./extract_replicates.py <input filename> <sequence identity cutoff> <length difference requirement> <initial base pair requirement> <output directory>

The <sequence identity cutoff> is cd-hits global sequence identity
calculated as the number of identical amino acids in the alignment
divided by the full length of the shorter sequence.

The <length difference requirement> is the percent of the sequence
that is required to match. 0 is the default and means that there is no
length restrictions.  This allows for reads of variable lengths.  1
will require that all the sequences in a cluster are the same length.

The <initial base pair requirement> is the number of base pairs
required to match at the beginning of each sequence.

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






