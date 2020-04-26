async function createMetaMaskDapp() {
	try {
		// Demande à MetaMask l'autorisation de se connecter
		const addresses = await ethereum.enable();
		const address = addresses[0]
		// Connection au noeud fourni par l'objet web3
		const provider = new ethers.providers.Web3Provider(ethereum);
		dapp = { address, provider };
		//console.log(dapp)
		return dapp;
	} catch(err) {
		// Gestion des erreurs
		console.error(err);
	}
}

async function balance(){
	dapp = await createMetaMaskDapp();
	dapp.provider.getBalance(dapp.address).then((balance) => {
		let etherString = ethers.utils.formatEther(balance);
		console.log("Balance: " + etherString);
		document.getElementById("balance").innerHTML = "Balance : "+etherString;
	});
	dapp.provider.getBlockNumber().then((bloc) => {
		console.log("Dernier bloc : " + bloc);
		document.getElementById("last_bloc").innerHTML = "Dernier bloc : "+bloc;
	});
	dapp.provider.getGasPrice().then((balance) => {
		let etherString = ethers.utils.formatEther(balance);
		console.log("Balance: " + etherString);
		document.getElementById("gaz").innerHTML = "Gaz : "+etherString;
	});
}