let CONTRACT_ABI = [
  {
    "constant": false,
    "inputs": [
      {
        "name": "dev",
        "type": "bytes32"
      }
    ],
    "name": "remettre",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "name": "cred",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "name": "dd",
        "type": "string"
      }
    ],
    "name": "produireHash",
    "outputs": [
      {
        "name": "",
        "type": "bytes32"
      }
    ],
    "payable": false,
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "name": "destinataire",
        "type": "address"
      },
      {
        "name": "valeur",
        "type": "uint256"
      }
    ],
    "name": "transfer",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
//let CONTRACT_ADDRESS = "0xfC3a6fE7B67679CCbACa927e4E30952F44553d55";
let CONTRACT_ADDRESS = "0x451875bdd0e524882550ec1ce52bcc4d0ff90eae";

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
	if (typeof dapp === "undefined") { await createMetaMaskDapp(); }
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

async function rendreDevoir(url) {
	if (typeof dapp === "undefined") { await createMetaMaskDapp(); }
	let contratCredibilite = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, dapp.provider.getSigner());
	var hashDevoir = contratCredibilite.produireHash(url);
	hashDevoir.then(function(hash) {
		console.log(contratCredibilite.remettre(hash));
		credibilite();
	})
	//credibilite();
	//console.log(hashDevoir.then);
	//remettre
}