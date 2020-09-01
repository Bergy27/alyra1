const Web3 = require('web3');
//const rpcURL = "https://ropsten.infura.io/v3/Your-Project-ID"
const rpcURL = "https://kovan.infura.io/v3/3f781f14af2945ee8d6d5030ecb546eb";
const web3 = new Web3(rpcURL);

/*const txObject = {
   nonce:    web3.utils.toHex(txCount),
   gasLimit: web3.utils.toHex(1000000), // Raise the gas limit to a much higher amount
   gasPrice: web3.utils.toHex(web3.utils.toWei('10', 'gwei')),
   data: data
 }*/
 
web3.eth.getBalance("0x9BF5d39830F95c9eFe02d6B764c6B76428147F92", (err, wei) => { 
   balance = web3.utils.fromWei(wei, 'ether'); // convertir la valeur en ether
   console.log(balance);
});


web3.eth.getTransactionCount("0x9BF5d39830F95c9eFe02d6B764c6B76428147F92", (err, txCount) => {
	console.log(txCount);
})