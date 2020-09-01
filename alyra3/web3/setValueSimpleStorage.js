const Web3 = require('web3');
var Tx = require('ethereumjs-tx').Transaction;
const rpcURL = "https://ropsten.infura.io/v3/3f781f14af2945ee8d6d5030ecb546eb";
const web3 = new Web3(rpcURL)
const ABI = [ { "constant": false, "inputs": [ { "internalType": "uint256", "name": "x", "type": "uint256" } ], "name": "set", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "get", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "storedData", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" } ];
const ADDRESS = "0xC6Ae1c2003Ab4D1a3e117Df1DAC07478f8919f4d";
const ACCOUNT = "0x9BF5d39830F95c9eFe02d6B764c6B76428147F92";
const privateKey1 = Buffer.from('A2EF4477230366820243B77B93153F42EC0D669D849FEA370EA6B9DA07EE5334', 'hex')

web3.eth.getTransactionCount(ACCOUNT, (err, txCount) => {
	const simpleStorage = new web3.eth.Contract(ABI, ADDRESS);
	const data = simpleStorage.methods.set(99).encodeABI();
	const txObject = {
		nonce: web3.utils.toHex(txCount),
		gasLimit: web3.utils.toHex(1000000), // Raise the gas limit to a much higher amount
		gasPrice: web3.utils.toHex(web3.utils.toWei('10', 'gwei')),
		to: ADDRESS,
		data: data
	}
	var tx = new Tx(txObject, {'chain':'ropsten'});
	tx.sign(privateKey1)
 
	const serializedTx = tx.serialize()
	const raw = '0x' + serializedTx.toString('hex')
 
	web3.eth.sendSignedTransaction(raw, (err, txHash) => {
		console.log('err:', err, 'txHash:', txHash)
		// Use this txHash to find the contract on Etherscan!
	})

})
