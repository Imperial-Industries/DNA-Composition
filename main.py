# Input sequence
# test_sequence = "ACAACATACAAAGGGCCACAGATACATCAAAAAATGCTCAACATCACTATTTGTCAGGGAAGTACTAATTAAAACCAAAATGAGATGTCCCCTCAAACCTGTTAGAATGGCTATTATCAAAAAGATGAAAGATAGCAACTATCAGAGAGGATGATAGAAAAGGGAACCCTTGCATCATGTACAAATTAAAAATAGAACTATCACATGATCCAAGAATCCTACTTCTGGGTATATAGCCAAAGGAATTGAAATCAATATGTCAAAGGGATATCTGCACTCCTATGTTATTGCAGCATGTTCACAATGGCCAAGATATAGAATCAACCTAACTGTTCATAGACAGATGAATGGATAAATGAAATGTGATATGGAAAATTATTCAGCCTTAAAAACAGTAGGAAATTCTGTCATTTGAGACAACGTGGATGAACCTAGAGGACATTAAGCTAAGTGAAATAAGCTAGACACAGAAAGACAAATATTGCATGATCTCACTTAGAATCTAAAAAATCTGAACTCATAGAAGCAGAGAATAGTATGATGGTTACTAGGGTTATCTGGCAGGGAGAGGATGAGGAAATGGGACATTGTTAATAAAAGGAAAAAAATTCAATTAGTAGG"
# The test_sequence was used to test if all of the functions worked correctly
homo_sapiens = open('hsapiens.txt').readlines()[0]
plasmodium_falciparum = open('pfalciparum.txt').readlines()[0]
common_mosquito = open('agambiaeas.txt').readlines()[0]
# Determining the length of the sequence
def length(string):
	length = 0;
	for i in string:
		# Make a function here that counts the number of nucleotides in the input 
		# sequence, return as variable "length".
		length = len(string)
	return length
# Counting the amount of Thymine in the sequence
def thymine_count(string):
    thymine_count = string.count('T')
    return thymine_count
# Counting the amount Adenine in the sequence
def adenine_count(string):
    adenine_count = string.count('A')
    return adenine_count
# Counting the amount of Cytosine in the sequence
def cytosine_count(string):
    cytosine_count = string.count('C')
    return cytosine_count
# Counting the amount of Guanine in the sequence
def guanine_count(string):
    guanine_count = string.count('G')
    return guanine_count
# Printing the results
print("Length: " + str(length(homo_sapiens)))
print("Thymine Count: " + str(thymine_count(homo_sapiens)))
print("Adenine Count: " + str(adenine_count(homo_sapiens)))
print("Cytosine Count: " + str(cytosine_count(homo_sapiens)))
print("Guanine Count: " + str(guanine_count(homo_sapiens)))
print("###")
print("Length: " + str(length(homo_sapiens)))
print("Thymine Count: " + str(thymine_count(plasmodium_falciparum)))
print("Adenine Count: " + str(adenine_count(plasmodium_falciparum)))
print("Cytosine Count: " + str(cytosine_count(plasmodium_falciparum)))
print("Guanine Count: " + str(guanine_count(plasmodium_falciparum)))
print("###")
print("Length: " + str(length(homo_sapiens)))
print("Thymine Count: " + str(thymine_count(common_mosquito)))
print("Adenine Count: " + str(adenine_count(common_mosquito)))
print("Cytosine Count: " + str(cytosine_count(common_mosquito)))
print("Guanine Count: " + str(guanine_count(common_mosquito)))
print("###")
