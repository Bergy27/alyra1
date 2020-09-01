const Web3 = require('web3')
const rpcURL = "https://ropsten.infura.io/v3/3f781f14af2945ee8d6d5030ecb546eb";
const web3 = new Web3(rpcURL)
const ABI = [
   {
       "constant": false,
       "inputs": [
           {
               "internalType": "uint256",
               "name": "x",
               "type": "uint256"
           }
       ],
       "name": "set",
       "outputs": [],
       "payable": false,
       "stateMutability": "nonpayable",
       "type": "function"
   },
   {
       "constant": true,
       "inputs": [],
       "name": "get",
       "outputs": [
           {
               "internalType": "uint256",
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
       "inputs": [],
       "name": "storedData",
       "outputs": [
           {
               "internalType": "uint256",
               "name": "",
               "type": "uint256"
           }
       ],
       "payable": false,
       "stateMutability": "view",
       "type": "function"
   }
];
const ADDRESS = "0xC6Ae1c2003Ab4D1a3e117Df1DAC07478f8919f4d";
const simpleStorage = new web3.eth.Contract(ABI, ADDRESS);
simpleStorage.methods.storedData().call((err, data) => {
   console.log(data);
});
