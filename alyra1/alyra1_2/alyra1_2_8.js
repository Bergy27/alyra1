const crypto = require('crypto');
const assert = require('assert');

chaines = process.argv.slice(2);

/*try {
	assert.strictEqual(chaines.length, 4);
} catch (err) {
	throw new Error("Vous devez rentrer exactement 4 paramètres")
}*/

function trouvePreuveParHauteur(noeudCourrant, merkle, hauteurAct, hauteurMax) {
	var indexCur = merkle.indexOf(noeudCourrant);
	if (indexCur==1) {
		console.log("Hauteur "+(hauteurMax-1)+" : "+merkle[2])
	} else if (indexCur==2) {
		console.log("Hauteur "+(hauteurMax-1)+" : "+merkle[1])
	} else {
		if (indexCur%2==0) {
			var indexFrere = indexCur-1;
		} else {
			var indexFrere = indexCur+1;
		}
		console.log("Hauteur "+hauteurAct+" : "+merkle[indexFrere]);

		trouvePreuveParHauteur(merkle[Math.floor((indexCur-1)/2)], merkle, hauteurAct+1, hauteurMax);
	}
	
}

function preuve(chaine, merkle) {
	var hauteur = Math.log(merkle.length+1)/(Math.log(2))-1;
	var hash = crypto.createHash('sha256').update(chaine).digest('hex');
	console.log("Condensat de "+chaine+" : "+hash);
	trouvePreuveParHauteur(hash, merkle, 0, hauteur)
}


function isPower2(number) {
	if (number==0) {
		return false;
	}
	return (number & (number - 1)) == 0;
}

while(!isPower2(chaines.length)) {
	chaines.push(null);
}

merkle = []
index = chaines.length-1
chaines.forEach(function(chaine) {
	if (chaine) {
		merkle[index] = crypto.createHash('sha256').update(chaine).digest('hex');
	} else {
		merkle[index] = null;
	}
	index++;
})
for (var i=chaines.length-2;i>=0;i--) {
	var gauche = merkle[2*i+1];
	var droite = merkle[2*i+2];
	if (gauche==null&&droite==null) {
		merkle[i] = null
	} else if (droite==null) {
		merkle[i] = gauche;
	} else {
		merkle[i] = crypto.createHash('sha256').update(gauche+droite).digest('hex');
	}
}
console.log(merkle);
var randomValue = Math.floor(Math.random()*chaines.length);
preuve(chaines[randomValue], merkle);