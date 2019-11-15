import sys
from functools import reduce


def search(bounds):
	return round(reduce((lambda x,y : x+y), bounds)/2)

def compare(solution, attempt, bounds):
	print("Ma proposition est {}".format(attempt))
	if solution-attempt>0:
		return {
			"found" : False,
			"bounds" : [attempt+1, bounds[1]]
		}
	elif solution-attempt<0:
		return {
			"found" : False,
			"bounds" : [bounds[0], attempt-1]
		}
	else:
		return {
			"found" : True,
			"bounds" : [bounds[0], attempt]
		}

try:
	solution = int(sys.argv[1])
except:
	print("Argument must be an integer")
	sys.exit(1)

assert solution>0 and solution<=100, "Argument must be between 1 and 100"

obj = {
	"found" : False,
	"bounds" : [1, 100] 
}

while not obj["found"]:
	mean = search(obj["bounds"])
	obj = compare(solution, mean, obj["bounds"])

print("Bravo, la réponse était {}".format(mean))
