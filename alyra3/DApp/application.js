let CONTRACT_ABI = [
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "bytes32",
				"name": "hash",
				"type": "bytes32"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "student",
				"type": "address"
			}
		],
		"name": "Remise",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "cred",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "hashs",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "url",
				"type": "string"
			}
		],
		"name": "produireHash",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "dev",
				"type": "bytes32"
			}
		],
		"name": "remettre",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "destinataire",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "valeur",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
let CONTRACT_ADDRESS = "0xeD508Fc6d77D9b937586cD242f4A80a8B687f1C8";

async function createMetaMaskDapp() {
	try {
		// Demande à MetaMask l'autorisation de se connecter
		const addresses = await ethereum.enable();
		const address = addresses[0]
		// Connection au noeud fourni par l'objet web3
		const provider = new ethers.providers.Web3Provider(ethereum);
		let monContrat=new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, provider);
		let monContratSigne=monContrat.connect(provider.getSigner(address.address));
		dapp = { provider, monContrat, monContratSigne, address}
		//dapp = { address, provider };

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
}

async function blockNumber() {
	if (typeof dapp === "undefined") { await createMetaMaskDapp(); }
		dapp.provider.getBlockNumber(dapp.address).then((blockNumber) => {
    	console.log("Dernier bloc: " + blockNumber);
    	document.getElementById("last_bloc").innerHTML = "Dernier bloc : "+blockNumber;
	});
}

async function gasPrice() {
	//if (typeof dapp === "undefined") { await createMetaMaskDapp(); }
	dapp = await createMetaMaskDapp();
	dapp.provider.getGasPrice(dapp.address).then((gasPrice) => {
		let etherString = ethers.utils.formatEther(gasPrice);
		console.log("Prix du gaz: " + etherString);
		document.getElementById("gaz").innerHTML = "Prix du gaz : "+etherString;
	});
}

async function credibilite() {
	if (typeof dapp === "undefined") { await createMetaMaskDapp(); }

	let contratCredibilite = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, dapp.provider.getSigner());
	let maCredibilite = await contratCredibilite.cred(dapp.address);
	console.log(maCredibilite);
	document.getElementById("credibilite").innerHTML = "Ma crédibilité est de : "+maCredibilite;
}

async function rendreDevoir() {
	if (typeof dapp === "undefined") { await createMetaMaskDapp(); }
	var url = document.getElementById("url").value;
	console.log(url);
	let contratCredibilite = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, dapp.provider.getSigner());
	var hash = await contratCredibilite.produireHash(url);
	let rank = await contratCredibilite.remettre(hash);

	contratCredibilite.on('Remise', (hash, student) => {
		console.log(hash);
		console.log(student);
	});
	console.log("Le devoir #" + rank + "a été remis");
}
