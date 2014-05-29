#!/usr/bin/python

import cgitb; cgitb.enable()
from repeats_html_template import HTML_TEMPLATE
import replicates_config
import cgi
import fasta
import os
import subprocess
import random
import tempfile
import sys
import time


form = cgi.FieldStorage()

dir = replicates_config.tmpdir

dirname = tempfile.mkdtemp('','',dir)
dirstub = dirname[len(dir):]

tmpurl = replicates_config.tmpurl

try:
   cdhit_input = open("%s/cdhit_input_temp.fa" % (dirname), 'w')
except:
    print "Content-type: text/html\n"
    print 'Cannot open', cdhit_input, 'for writing'
    sys.exit(2)
                                    
if not form.has_key("filename"):
    print 'Location: %s\n' % replicates_config.url 
    sys.exit(0)

cutoff_input = form.getvalue('cutoff')
try:
    cutoff_test = float(cutoff_input)
    if (cutoff_test > 1.0 or cutoff_test < 0.85):
        print "Content-type: text/html\n"
        print "Please input a cutoff value between 0.85 and 1.0"
        sys.exit(2)
    else:
        cutoff = cutoff_test

except ValueError:
    print "Content-type: text/html\n"
    print "Please input a cutoff value between 0.85 and 1.0"
    sys.exit(2)
 
length_input = form.getvalue('length')
try:
    length_test = float(length_input)
    if (length_test > 1.0):
        print "Content-tyoe: text/html\n"
        print "Please input a length requirement value between 0 and 1.0"
        sys.exit(2)
    else:
        length = length_test
except ValueError:
    print "Content-tyoe: text/html\n"
    print "Please input a length requirement value between 0 and 1.0"
    sys.exit(2)

bp_input = form.getvalue('bp')

email = form.getvalue('email')

item=form["filename"]
   
if not item.file:
   print "Content-type: text/html\n"
   print 'Please upload a file'
   sys.exit(2)

data = item.file
input_filename = item.filename


try:
   fasta_data = fasta.load(data)
except:
   print "Content-type: text/html\n"
   print 'This file does not seem to be a fasta file.  Please try again with a fasta file'
   sys.exit(0)

fp = open('%s/index.html' % (dirname,), 'w')
fp.write('''
<head><META http-equiv="refresh" content="2;URL=%s/%s/index.html"></head>
<body>
<table border=1 noshade align=center cellspacing=0 width=600 cellpadding=15>
<tr><td bgcolor=#FF6600>&nbsp;
<tr><td>
<p>This page will automatically reload, and the results will be available here.  
<p>If you get a blank page, hit Reload on your browser.
<p>Results for large datasets can take up to 20 minutes to be returned ...
</table>
</body>
''' % (tmpurl, dirstub,))
fp.close()

print 'Location: %s/%s\n' % (tmpurl, dirstub,)

if os.fork() != 0:
    sys.exit(0)

# run in child process; daemonize first
si = file("/dev/null", 'r')
so = file("/dev/null", 'a+')
se = file("/dev/null", 'a+', 0)
os.dup2(si.fileno(), sys.stdin.fileno())
os.dup2(so.fileno(), sys.stdout.fileno())
os.dup2(se.fileno(), sys.stderr.fileno())

os.setsid()

# Print this data out to a file for cd-hit to run
# This is better than uploading the file, because you don't have security issues,
# you can make sure it's fasta, and you aren't writing a lot of files to disk

for key in fasta_data:
    cdhit_input.write('>%s\n%s\n' % (key, fasta_data[key]))
cdhit_input.close()

# The output file from cd-hit is written to the tmp directory for this session

cdhit_command = '%s/cd-hit-est -i %s/cdhit_input_temp.fa -o %s/cdhit_output_temp -c %s -n 8 -s %s -d 0' % (replicates_config.cdhit_dir, dirname, dirname, cutoff, length)


# Run CD-HIT
prog = subprocess.Popen(cdhit_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

(stdout, stderr) = prog.communicate()

fp = open(dirname+'/cd-hit.out', 'w')
fp.write(stdout)
fp.close()

fp = open(dirname+'/cd-hit.err', 'w')
fp.write(stderr)
fp.close()

output_filename = 'extracted_clusters'

# Evaluate CD-HIT files
prog2 = subprocess.Popen('%s/extract-clusters-html.py %s/cdhit_output_temp.clstr  %s/cdhit_input_temp.fa %s/%s %s html -i "%s"' % (replicates_config.cdhit_dir, dirname, dirname, dirname, output_filename, bp_input, input_filename), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

(stdout, stderr) = prog2.communicate()



fp = open(dirname+'/extract.out', 'w')
fp.write(stdout)
fp.write ('%s/extract-clusters-html.py %s/cdhit_output_temp.clstr  %s/cdhit_input_temp.fa %s/%s %s html -i %s' % (replicates_config.cdhit_dir, dirname, dirname, dirname, output_filename, bp_input, input_filename),)
fp.close()

fp = open(dirname+'/extract.err', 'w')
fp.write(stderr)
fp.close()


# Load the *.clstr file
# Process that file


f = open('%s/index.html' % (dirname),'w')


f.write (HTML_TEMPLATE % (input_filename, cutoff, length, bp_input, stdout, tmpurl, dirstub, output_filename, tmpurl, dirstub, output_filename, tmpurl, dirstub, output_filename))
   
if (len(email) > 1):
   mail_command = 'echo The analysis for your file %s is finished and is available at %s | mail %s -s Replicates results' % (input_filename, tmpurl, email)
   prog3 = subprocess.Popen(mail_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

   (stdout, stderr) = prog3.communicate()

   fp = open(dirname+'/email.out', 'w')
   fp.write(stdout)
   fp.close()

   fp = open(dirname+'/email.err', 'w')
   fp.write(stderr)
   fp.close()
