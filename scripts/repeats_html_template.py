HTML_TEMPLATE = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/
                                                                DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<!--
Copyright: Darren Hester 2006, http://www.designsbydarren.com
License: Released Under the "Creative Commons License", http://creativecommons.org/licenses/by-nc/2.5/
-->

<head>

<!-- Meta Data -->
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" /><meta name="description" content="Free 2-Column CSS Web Design Template" /><meta name="keywords" content="Free, 2-Column, CSS, Web, Design, Template" />

<!-- Site Title -->
<title>454 Replicate Filter</title>

<!-- Link to Style External Sheet -->
<link href="../../css/style.css" type="text/css" rel="stylesheet" />

</head>

<body>

<div id="page_wrapper">

<div id="page_header">
<h1>Schmidt Lab</h1>
<h2>Power, efficiency and microbial communities</h2>

</div>

<div id="menu_bar">
<ul>
<li><a href="#">Home</a></li>
<li><a href="#">Research</a></li>
<li><a href="#">Data</a></li>
<li><a href="#">Software</a></li>
<li><a href="#">Protocols</a></li>
</ul>
</div>

<div id="content_wrapper">

<div id="left_side">

<h2>454 Replicate Filter</h2>


<h3>Data summary</h3>

File: %s
<br>Evaluated with:<br> cutoff %s, length requirement %s0 and initial base pair match %s

%s


<h3>Files</h3>
<p>Right click or Control-click on the file name and you will be able to download it.
<table>
<tr><td>Set of unique reads:</td> <td><a href=%s/%s/%s_unique.fa>Fasta file</a></td></tr>
<tr><td>Summary of clusters: <td><a href=%s/%s/%s.cluster_summary>cluster summary text</a>
<tr><td>Sequences in each cluster: <td><a href=%s/%s/%s.fasta_clusters>cluster list</a>
</table>

<p>--------------------------------
<br>Version 1.0 - updated March 26, 2009
</div>

<div id="right_side">


<p class="block"><strong>Note: </strong>
Sequences that cluster together by <a href=http://www.bioinformatics.org/cd-hit/>CD\
-HIT</a> and start
with the same beginning base pairs are identified as replicates and clustered.
If many sequences are expected to look similiar and start at the same position, thi\
s is not
the right tool for your data, e.g. 454 tag data.
<p class="block"><strong>Availability:</strong>
<br>These scripts are all open source and distributed under the Gnu GPL.  They can also be run at the command line witho\
ut the web interface.  They are currently available if you contact the authors and will be made available here soon.

<p class="block"><strong>Comments/Questions:</strong>
<br>If you have any comments or questions about these programs, please contact the \
<a href=mailto:tkteal@msu.edu>authors</a>.
</div>



</div>




<div id="page_footer">
<p><font size=-2>&nbsp;<br />

<!--
<a href="http://validator.w3.org/check?uri=referer" target="_blank">Valid XHTML 1.0 Transitional</a></p></font>
-->
</div>

</div>

</body>
</html>
"""
