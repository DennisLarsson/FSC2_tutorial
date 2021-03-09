import sys
import os

popmap_path = sys.argv[1]
vcf_path = sys.argv[2]
list_path = vcf_path.split("/")
list_path.pop()
vcf_wd = "/".join(list_path)
vcf_wd = vcf_wd + "/"
popmap = []
with open (popmap_path) as popmap_file:
	for i in popmap_file:
		popmap.append(i.rstrip().split("\t"))

os.system('grep "#" ' + vcf_path + ' > ' + vcf_wd + 'temp_vcfheader')
os.system('grep  -v "#" ' + vcf_path + ' > ' + vcf_wd + 'temp_vcfcontent')

vcfheader_list = []
with open (vcf_wd + 'temp_vcfheader') as vcfheader_file:
	vcfheader_list = vcfheader_file.readlines()

vcfheader_list.pop()
names_line_start = '#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT'

name_line = ""
for i in popmap:
	indv = i[0].replace("_","")
	new_name = indv + "." + i[1]
	name_line = name_line + "\t" + new_name

names_line = names_line_start + name_line + "\n"

vcfheader_list.append(names_line)

with open (vcf_wd + 'temp_vcfheader_new','w') as new_vcfheader_file:
	for i in vcfheader_list:
		new_vcfheader_file.write(i)

vcf_path_new_list = vcf_path.split(".")
vcf_path_new_list.pop()

vcf_path_new = ".".join(vcf_path_new_list)
vcf_path_new = vcf_path_new + ".renamed.vcf"
os.system('cat ' + vcf_wd + 'temp_vcfheader_new ' + vcf_wd + 'temp_vcfcontent > ' + vcf_path_new)

os.system('rm ' + vcf_wd + 'temp_vcfheader ' + vcf_wd + 'temp_vcfcontent ' + vcf_wd + 'temp_vcfheader_new')

with open (vcf_wd + 'new_popmap','w') as new_popmap_file:
	for i in popmap:
		indv = i[0].replace("_","")
		indv = indv + "." + i[1]
		new_popmap_file.write(indv + "\t" + i[1] + "\n")