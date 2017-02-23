//$(document).ready(function() {

		var Web3 = require('web3');
		var web3 = new Web3();

		rpcport = localStorage.getItem('rpcport');
		//web3.setProvider(new web3.providers.HttpProvider());
		//default port is 8545

		web3.setProvider(new web3.providers.HttpProvider("http://localhost:"+JSON.stringify(rpcport)));

		function watchBalance() {

		    console.log('11111');

		    var coinbase = web3.eth.coinbase;
		    console.log(coinbase);
		    var originalBalance = web3.eth.getBalance(coinbase).toNumber();

		    console.log(originalBalance);
		    document.getElementById('coinbase').innerText = 'coinbase: ' + coinbase;
		    document.getElementById('original').innerText = ' original balance: ' + originalBalance + '    watching...';

		    web3.eth.filter('latest').watch(function() {
		        var currentBalance = web3.eth.getBalance(coinbase).toNumber();
		        document.getElementById("current").innerText = 'current: ' + currentBalance;
		        document.getElementById("diff").innerText = 'diff:    ' + (currentBalance - originalBalance);
		    });
		}

//});