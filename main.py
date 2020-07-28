# Input sequence
test_sequence = "ACAACATACAAAGGGCCACAGATACATCAAAAAATGCTCAACATCACTATTTGTCAGGGAAGTACTAATTAAAACCAAAATGAGATGTCCCCTCAAACCTGTTAGAATGGCTATTATCAAAAAGATGAAAGATAGCAACTATCAGAGAGGATGATAGAAAAGGGAACCCTTGCATCATGTACAAATTAAAAATAGAACTATCACATGATCCAAGAATCCTACTTCTGGGTATATAGCCAAAGGAATTGAAATCAATATGTCAAAGGGATATCTGCACTCCTATGTTATTGCAGCATGTTCACAATGGCCAAGATATAGAATCAACCTAACTGTTCATAGACAGATGAATGGATAAATGAAATGTGATATGGAAAATTATTCAGCCTTAAAAACAGTAGGAAATTCTGTCATTTGAGACAACGTGGATGAACCTAGAGGACATTAAGCTAAGTGAAATAAGCTAGACACAGAAAGACAAATATTGCATGATCTCACTTAGAATCTAAAAAATCTGAACTCATAGAAGCAGAGAATAGTATGATGGTTACTAGGGTTATCTGGCAGGGAGAGGATGAGGAAATGGGACATTGTTAATAAAAGGAAAAAAATTCAATTAGTAGG"
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
print("Length: " + str(length(test_sequence)))
print("Thymine Count: " + str(thymine_count(test_sequence)))
print("Adenine Count: " + str(adenine_count(test_sequence)))
print("Cytosine Count: " + str(cytosine_count(test_sequence)))
print("Guanine Count: " + str(guanine_count(test_sequence)))
