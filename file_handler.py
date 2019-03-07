def make_content_from_file(filename):
	file = open(filename,"r")
	content = [line.rstrip('\n') for line in file]
	file.close()
	return content

def get_rules_from_file():
	file = open("rules.txt","r")
	rules = [line.rstrip('\n') for line in file]
	file.close()
	return rules


