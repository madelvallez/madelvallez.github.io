//livre1 : id html
//l1: nb de page lu entré par util


function resu() {
	var l1 = parseInt(document.getElementById("Livre1").value);
	l1 = isNaN(l1) ? 0 : l1;
	var l2 = parseInt(document.getElementById("Livre2").value);
	l2 = isNaN(l2) ? 0 : l2;
	var l3 = parseInt(document.getElementById("Livre3").value);
	l3 = isNaN(l3) ? 0 : l3;
	var l4 = parseInt(document.getElementById("Livre4").value);
	l4 = isNaN(l4) ? 0 : l4;
	var l5 = parseInt(document.getElementById("Livre5").value);
	l5 = isNaN(l5) ? 0 : l5;
	var l6 = parseInt(document.getElementById("Livre6").value);
	l6 = isNaN(l6) ? 0 : l6;

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
	
	var pages = 745 - (l1 + l2 + l3 + l4 + l5 + l6) ;
	
	var vitesse = pages / temps ;
	
	document.getElementById("A-lire").innerHTML=pages ;
	document.getElementById("EnJour").innerHTML=temps ;
	document.getElementById("LireParJour").innerHTML=vitesse.toFixed(2) ;
	
}
