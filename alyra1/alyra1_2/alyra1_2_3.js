function factoOptimise(n) {
	return multImpaireInf(n)*multImpaireInf(Math.floor(n/2))*multImpaireInf(Math.floor(n/2)-2)*2**findPower(Math.floor(n/2));
}


function findPower(n) {
	if (n==1) {
		return 1;
	}
	return n+findPower(Math.floor(n/2));
}

function secondTerm(n) {
	if (n==1||n==2) {
		return 1
	} else {
		return multImpaireInf(n)*secondTerm(n-2)
	}
}

function multImpaireInf(n) {
	if (n==1) {
		return 1;
	} else {
		if (n%2==0) {
			return (n-1)*multImpaireInf(n-3);
		} else {
			return n*multImpaireInf(n-2);
		}
	}
}

console.log(factoOptimise(7));
console.log(factoOptimise(12));

