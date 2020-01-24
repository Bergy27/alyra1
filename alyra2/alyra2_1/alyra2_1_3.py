def blocReajustement(numBlock):
	if numBlock%2016==0:
		return True
	return False

print(blocReajustement(0))
print(blocReajustement(2016))
print(blocReajustement(2017))
print(blocReajustement(556416))