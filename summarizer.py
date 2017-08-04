import re
import sys
def main(argv):
	try:
		filename = argv[1]
	except:
		print("Please specify input file")
		quit()

	with open(filename) as f:
		block = f.read()

	sentences = re.split("(?<=\.|!)\s(?=[A-Z])",block)
	words = re.split("[\n\s]",re.sub("[^\w\s]","",block).lower())
	wordcount = {}

	for word in words:
		try:
			wordcount[word] += 1
		except:
			wordcount[word] = 1
	
	sScores = []
	for i in range(0,len(sentences)):
		sentence = sentences[i]
		sentenceWords = re.split("[\n\s]",re.sub("[^\w\s]","",sentence).lower())
		score = 0
		for word in sentenceWords:
			score += 1/wordcount[word]
		sScores.append(score/len(sentenceWords))

	print(sentences[sScores.index(max(sScores))])
		
main(sys.argv)
