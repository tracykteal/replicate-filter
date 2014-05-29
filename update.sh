#! /bin/bash
cp ~/replicates/cgi-bin/* /var/sites/microbiomes.msu.edu/www/cgi-bin
cp -r ~/replicates/html/* /var/sites/microbiomes.msu.edu/www/html/replicates
cp ~/replicates/scripts/* /var/sites/microbiomes.msu.edu/www/cgi-bin/cd-hit

cp ~/replicates/scripts/replicates_config.py /var/sites/microbiomes.msu.edu/www/cgi-bin/replicates_config.py

cp ~/replicates/scripts/repeats_html_template.py /var/sites/microbiomes.msu.edu/www/cgi-bin/repeats_html_template.py

cp ~/replicates/scripts/fasta.py /var/sites/microbiomes.msu.edu/www/cgi-bin/fasta.py