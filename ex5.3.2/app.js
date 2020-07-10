
function showList(list) {
	list += "</ul>"
	document.getElementById("list").innerHTML = list;
}

function ping() {
	const ipfs = window.IpfsHttpClient('localhost', '5001');
	let ctr = 0;
	ipfs.swarm.addrs().then(function(addresses) {
		let list = "<ul>"
		addresses.slice(0,10).forEach(function(address) {
			ipfs.ping(address.id._idB58String).then(function(result) {
				ctr++;
				list+= "<li>Connect to node "+address.id._idB58String+" : Success</li>";
				if (ctr==10) {
					showList(list);
				}
			}).catch(function(error) {
				ctr++;
				list += "<li>Connect to node "+address.id._idB58String+" : Failed</li>";
				if (ctr==10) {
					showList(list);
				}
				console.log(error);
			})
		})
	})
}