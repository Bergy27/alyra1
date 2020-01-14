#python3 alyra1_4_6.py "4" "2" "*" "8" "=" --> True (ok)
#python3 alyra1_4_6.py "4" "5" "3" "<" "+" --> 4 (ok)
#python3 alyra1_4_6.py "4" "5" "3" ">" "+" --> 5 (ok)
#python3 alyra1_4_6.py "4" "3" "<" --> False (ok)
#True=1
#False=0
import sys


def calcPolonaiseInversee(pile, tas):
	#print("Pile  : "+str(pile))
	#print("Tas : "+str(tas))
	if len(tas)==0:
		return pile[0]
	if tas[0] in ["+", "*", "-", "/", "<", ">", "="]:
		arg2 = int(pile.pop())
		arg1 = int(pile.pop())
		if tas[0]=="+":
			return calcPolonaiseInversee(pile+[arg1+arg2], tas[1:])
		elif tas[0]=="-":
			return calcPolonaiseInversee(pile+[arg1-arg2], tas[1:])
		elif tas[0]=="*":
			return calcPolonaiseInversee(pile+[arg1*arg2], tas[1:])
		elif tas[0]=="/":
			return calcPolonaiseInversee(pile+[arg1/arg2], tas[1:])
		elif tas[0]==">":
			return calcPolonaiseInversee(pile+[arg1>arg2], tas[1:])
		elif tas[0]=="<":
			return calcPolonaiseInversee(pile+[arg1<arg2], tas[1:])
		elif tas[0]=="=":
			return calcPolonaiseInversee(pile+[arg1==arg2], tas[1:])
	else:
		 return calcPolonaiseInversee(pile+[tas[0]], tas[1:])

a = calcPolonaiseInversee([], sys.argv[1:])
print(a)