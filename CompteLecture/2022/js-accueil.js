//Livre1 : id html
//livre1 : elem html du Livre1
//l1: nb de page lu entré par util

function initMinMax() {
	var pagesTotal = 0;
	var inputNumberList = document.querySelectorAll("span.field input[type=number]");
	for ( var inputElt of inputNumberList) {
		var minVal = inputElt.min;
		var maxVal = inputElt.max;
		var minStr = isNaN(minVal) ? "ND 0" : minVal;
		var minVal = isNaN(minVal) ? 0 : minVal;
		var maxStr = isNaN(maxVal) ? "ND ERR" : maxVal;
		var maxVal = isNaN(maxVal) ? undefined : maxVal;
		var noteElt = inputElt.parentElement.querySelector("span.note");
		noteElt.innerText = " min: "+minStr+" - max: "+maxStr;
		if ( maxVal != undefined ) {
			pagesTotal += maxVal - minVal + 1 ;
		}
	}
	var totalElt = document.getElementById("total");
	totalElt.innerText = " / "+ pagesTotal;
}

function resu() {
	var livre1 = document.getElementById("Livre1");
	var l1 = parseInt(livre1.value);
	var min_l1 = parseInt(livre1.getAttribute("min"));
	l1 = isNaN(l1) ? min_l1 : l1;

	var livre2 = document.getElementById("Livre2");
	var l2 = parseInt(livre2.value);
	var min_l2 = parseInt(livre2.getAttribute("min"));
	l2 = isNaN(l2) ? 49 : l2;

	var livre3 = document.getElementById("Livre3");
	var l3 = parseInt(livre3.value);
	var min_l3 = parseInt(livre3.getAttribute("min"));
	l3 = isNaN(l3) ? min_l3 : l3;

	var livre4 = document.getElementById("Livre4");
	var l4 = parseInt(livre4.value);
	var min_l4 = parseInt(livre4.getAttribute("min"));
	l4 = isNaN(l4) ? min_l4 : l4;

	var livre5 = document.getElementById("Livre5");
	var l5 = parseInt(livre5.value);
	var min_l5 = parseInt(livre5.getAttribute("min"));
	l5 = isNaN(l5) ? min_l5 : l5;

	var livre6 = document.getElementById("Livre6");
	var l6 = parseInt(livre6.value);
	var min_l6 = parseInt(livre6.getAttribute("min"));
	l6 = isNaN(l6) ? min_l6 : l6;


	var date = document.getElementById("jour").valueAsDate;
	if ( date === null ) { 
		date = new Date();
		date.setUTCHours(0, 0, 0, 0);
		document.getElementById("jour").valueAsDate=date;
	}
	var date_fin = document.getElementById("dernier").valueAsDate;
	if ( date_fin === null ) { 
		date_fin = new Date("2022-08-29");
		date_fin.setUTCHours(0, 0, 0, 0);
		document.getElementById("dernier").valueAsDate=date_fin;
	}
	
	var diff = date_fin.getTime() - date.getTime();
	var temps = diff / (1000 * 3600 * 24); 

	var nb_l1 = l1 - min_l1;
	var nb_l2 = l2 - min_l2;
	var nb_l3 = l3 - min_l3;
	var nb_l4 = l4 - min_l4;
	var nb_l5 = l5 - min_l5;
	var nb_l6 = l6 - min_l6;
	
	// max encore en dur ...
	var pages = 745 - (nb_l1 + nb_l2 + nb_l3 + nb_l4 + nb_l5 + nb_l6) ;
	
	var vitesse = pages / temps ;
	
	document.getElementById("A-lire").innerHTML=pages ;
	document.getElementById("EnJour").innerHTML=temps ;
	document.getElementById("LireParJour").innerHTML=vitesse.toFixed(2) ;
	
}
