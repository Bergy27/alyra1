const ipfs = window.IpfsHttpClient('localhost', '5001');
const CONTRACT_ADDRESS = "0x385f2af3F5fD5D4ECc31992ef803318552B20A45";
const CONTRACT_ABI = '[{"constant":false,"inputs":[{"internalType":"string","name":"s","type":"string"}],"name":"ajouterCarte","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"ind","type":"uint256"}],"name":"recuperer","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]';

let dapp;

function envoyerSurIpfs(str) {
	ipfs.add(new ipfs.types.Buffer.from(str)).then(function(result) {
		ipfs.pin.add(result[0].hash);
		ajouterCarteContract(result[0].hash);
	})
}

function _arrayBufferToBase64(buffer) {
    var binary = '';
    var bytes = new Uint8Array( buffer );
    var len = bytes.byteLength;
    for (var i = 0; i < len; i++) {
        binary += String.fromCharCode( bytes[ i ] );
    }
    return window.btoa(binary);
}


function ajouterCarte() {
	let image = document.getElementById("carte");
	const reader = new FileReader();
	reader.readAsArrayBuffer(image.files[0]);
	reader.onloadend = function () {
		envoyerSurIpfs(_arrayBufferToBase64(reader.result));
	}
}

async function createMetaMaskDapp() {
  try {
    // Demande à MetaMask l'autorisation de se connecter
    const addresses = await ethereum.enable();
    const address = addresses[0];
    // Connection au noeud fourni par l'objet web3
    const provider = new ethers.providers.Web3Provider(ethereum);
    dapp = { address, provider };
  } catch (err) {
    // Gestion des erreurs
    console.error(err);
  }
}

function getImage(code) {	
	return ipfs.get(code);
}

async function ajouterCarteContract(code) {
	let contrat = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, dapp.provider.getSigner());
	await contrat.ajouterCarte(code);
	listerCartes();
}

async function listerCartes() {
	if (typeof dapp === "undefined") { await createMetaMaskDapp(); }
	let contrat = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, dapp.provider.getSigner());
	let response;
	let image;
	let imageBase64;
	let images = [];
	let listeCartesHtml = "<ul>";
	for (let i=0;i<10;i++) {
		try {
			image = await contrat.recuperer(i);
			imageBase64 = await getImage(image);
			listeCartesHtml += '<li><img src="data:image/jpg;base64,'+imageBase64[0].content+'" width="200px" height="200px" </li>';
		} catch(e) {
			console.log("index does not existing !");
		}		
	}
	listeCartesHtml += "</ul>";
	document.getElementById("cartes").innerHTML = listeCartesHtml; 
}

async function init() {
	if (typeof dapp === "undefined") { await createMetaMaskDapp(); }
	listerCartes();
}