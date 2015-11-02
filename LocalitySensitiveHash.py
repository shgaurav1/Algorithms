

Attachment GauravShrivastava_Resume.pdf successfully uploaded and added.Conversation opened. 1 read message.

Skip to content
Using Gmail with screen readers
Gaurav
Yesware
Search


lsh 


TRIAL  Events   Emails   Scheduled   Reminders  
29%
 Get Started EXPAND
Gmail
COMPOSE MAIL MERGE
Labels
Inbox
Starred
Important
Sent Mail
Drafts (7)
Circles
More 
Hangouts

 
 
Move to Inbox More  Tracking    Reminder 
4 of 4  
 
Print all In new window
LSH codes in python
Inbox
x 

Harsh Shrivastava <harsh.shrivastava91@gmail.com>
AttachmentsJul 25
Log to Salesforce		
to me 

Attachments area
Preview attachment lsh_copy.py

Text
lsh_copy.py
	
Click here to Reply or Forward
2.63 GB (17%) of 15 GB used
Manage
Terms - Privacy
Last account activity: 14 minutes ago
Details
Harsh Shrivastava's profile photo
Harsh Shrivastava
Add to circles

Show details
Salesforce

Compose:
New Message
MinimizePop-outClose
# code for 1. Creating shingles matrix; 2. Minhashing; 3. Locality sensitive hashing

# Making shingles from the document sen.txt
import os, sys, binascii, random, pickle
SHINGLES_EXTRACTED = 0
SHINGLE_length = 3 # k-shingles
NUM_HASH = 1000 # number of signature functions
nextPrime = 4294967311
createSIGNATURE_MAT = 0
LSH_DONE = 0
ROWS_PER_BAND = 4
BANDS = int(NUM_HASH/ROWS_PER_BAND)
NUM_LSH_BUCKETS = 100000000


def extract_shingles_dict(sentences):# shingles_dict = {'shingle': [sentence in which shingle present]}
    shingles_dict = {}
    line_number = 0
    for line in file(sentences):
        line_number += 1
        line = line.strip() # each line is a sentence
        line = line.split(' ') # splitting each line with a space
        sentence = ''
        sentence = ' '.join(line[1::]) # extracting the sentence from the line 
        sentence_number = line[0]
#        print sentence_number
        for i in range(0, len(sentence)-SHINGLE_length+1): # for each line 
            shingle = sentence[i:i+SHINGLE_length]
#            print sentence
#            print shingle
            if shingle not in shingles_dict:
                shingles_dict[shingle] = [sentence_number]
            else:
                if sentence_number not in shingles_dict[shingle]:
                    shingles_dict[shingle].append(sentence_number) 

        if line_number%10000 == 0:
            print line_number 
#            break
#    print shingles_dict
    # save the dictionary using pickle
    with open('shingles_dict.pickle', 'w') as fid:
        pickle.dump(shingles_dict, fid)
    return shingles_dict

def get_shingles(filename):
	text_file = open(filename, "r")
	words_array = []
	line_num = 0


#	total_lines = len(text_file.readlines())
#	text_file.close()
#	text_file = open(filename, "r")
#	words_array = text_file.read().split()
#	print words_array
#	num_array = [str(x) for x in range(total_lines)]
#	print num_array
#	print total_lines
#	print len(words_array)	
#	shingles = set(words_array).difference(set(num_array))
#	shingles_list = list(shingles)



	for line in file(filename):
		line_num += 1
		line = line.strip() # each line is a sentence
		line = line.split(' ')
		for i in range(1, len(line)):
			words_array.append(line[i])
		if line_num%10000 == 0:
			print line_num
#		if line_num == 100:
#			print 'Press any key to continue'
#			raw_input()
#			print words_array

	print 'length of words_array = ' + str(len(words_array))

	shingles = set(words_array)
	shingles_list = list(shingles)
	print 'length of shingles list = '+ str(len(shingles_list))
#	print shingles_list[0:100]
	return shingles_list, line_num

def sentence_search(word, sentence):
#	print sentence
#	sentence = sentence.split(' ')
#	print sentence
	result = False
	for i in range(1, len(sentence)):
		if sentence[i]==word:
			result = True
			break
	return result


# Our random hash function will take the form of:
#   h(x) = (a*x + b) % c
# Where 'x' is the input value, 'a' and 'b' are random coefficients, and 'c' is
# a prime number just greater than maxshingle value.

def hash_functions(x, a, b): # returns h(x)
	# here we define 100 hash functions and store their value in an array H
	h = [0 for j in range(NUM_HASH)]
	for i in range(0, NUM_HASH):
		h[i] = ((a[i]+1)*x+b[i])%nextPrime
	return h
	

def minhash(filename, shingles_list, total_sentences):
	R = len(shingles_list)
	C = total_sentences
	M = [[NUM_HASH+1 for x in range(C)] for x in range(NUM_HASH)] # matrix of SIG x C dimensions:  initialise it to 101 as the hash functions here are defined as mod 100
	text_file = open(filename, 'r')
	words_array = []
	text_array = text_file.readlines()
	for string in text_array:
		words_array.append(string.split())
	for r in range(0, R):# for each row r
		print r
#		for i in range(0, NUM_HASH):# for calculate h(r) for each hash function
		h = hash_functions(r) # h = array[0, NUM_HASH-1] containing the hash values of NUM_HASH different hash functions
		for c in range(0, C): # for each sentence update the minhash matrix if the word is present in the sentence
			if sentence_search(shingles_list[r], words_array[c]) == True:
				for i in range(0, NUM_HASH):
					if h[i]<M[i][c]:
						M[i][c] = h[i]
	return M

def hash1(shingle):
	return binascii.crc32(shingle) & 0xffffffff

def hash_minhash(filename, shingles_list, total_sentences):
	C = total_sentences
	M = [[nextPrime+1 for x in range(C)] for x in range(NUM_HASH)] # matrix of SIG x C dimensions:  initialise it to 101 as the hash functions here are defined as mod 100
	text_file = open(filename, 'r')
	words_array = []
	text_array = text_file.readlines()

	maxShingle_value = 2**32-1
	a_vec = [random.randint(0, maxShingle_value) for x in range(NUM_HASH)] 
	b_vec = [random.randint(0, maxShingle_value) for x in range(NUM_HASH)] 

	for string in text_array:
		words_array.append(string.split())
	for c in range(0, C):
		for shingle in range(1, len(words_array[c])):
			# hash the word to binascii format = hash1
			hash_shingle = hash1(words_array[c][shingle])
			h = hash_functions(hash_shingle, a_vec, b_vec)
		for i in range(0, NUM_HASH):
			if h[i]<M[i][c]:
				M[i][c] = h[i]
	return M	

def create_LSH_buckets(M, C):# candidate pairs buckets from signature matrix
	b = BANDS
	r = ROWS_PER_BAND
	BUCKET_DICT = {} # the max number of buckets depends on the K = BUCKETS_HASH_FUNCTIONS's mod value chosen
	for col in range(0, C):# for each column
		sum_row = 0
		for row in range(0, NUM_HASH): # for each row
		# use hash functions called BUCKET_HASH_FUNCTIONS on the set of bands
		# Applying hash function on the sum of rows in a band
			sum_row += M[row][col]
			if row>0 and row%5==0:
				bucket_num = sum_row % NUM_LSH_BUCKETS # hashing function for the signature matrix to bucket mapping
				# add the particular bucket and the corresponding column to the BUCKET_DICT
				if bucket_num not in BUCKET_DICT:
					BUCKET_DICT[bucket_num] = [col]
				else:
					BUCKET_DICT[bucket_num].append(col)
				sum_row = 0
	return BUCKET_DICT
		
def main():
	if sys.argv[1]<1:
		print 'Usage:python make_shingles.py sentences.txt'
		exit(0)
	sentence_file = sys.argv[1]
	sentence_filename = os.path.splitext(sentence_file)[0]
	if SHINGLES_EXTRACTED == 0: # here shingles are words...
		#shingles_dict = extract_shingles_dict(sentences)
		shingles_list, total_sentences = get_shingles(sentence_file) # set of unique words which will constitute the rows of shingles matrix
#	M = minhash(sentence_file, shingles_list, total_sentences)
	print 'Shingles extracted'
	print 'Creating Signature Matrix'
	if createSIGNATURE_MAT == 0:
		M = hash_minhash(sentence_file, shingles_list, total_sentences)
		print 'Signature Matrix created'
#	print M
	print 'Creating candidate pairs buckets'
	if LSH_DONE == 0:
		compare_dict = create_LSH_buckets(M, total_sentences) # generate candidate pairs from signature matrix M
	print 'Candidate pairs generated for comparison'
	print 'Saving Signature Matrix and compare dictionary'
	with open('sig_mat_buckets_'+sentence_filename+'.pickle', 'w') as fid:
		pickle.dump([M, compare_dict], fid)
	print 'Files saved'
	print compare_dict

if __name__=="__main__":
    main()
lsh_copy.pyOpen
Displaying lsh_copy.py.
