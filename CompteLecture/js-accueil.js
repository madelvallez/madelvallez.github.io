function resu() {
	var emile = parseInt(document.getElementById("stadeEmile").value);
	emile = isNaN(emile) ? 0 : emile;
	var contes = parseInt(document.getElementById("stadeAndersen").value);
	contes = isNaN(contes) ? 0 : contes;
	var ake = parseInt(document.getElementById("stadeAke").value);
	ake = isNaN(ake) ? 0 : ake;
	var date = document.getElementById("jour").valueAsDate;
	if ( date === null ) { 
		date = new Date();
		date.setUTCHours(0, 0, 0, 0);
		document.getElementById("jour").valueAsDate=date;
	}
	
	var date_fin = new Date("2021-08-29");
	var diff = date_fin.getTime() - date.getTime();
	var temps = diff / (1000 * 3600 * 24); 
	
	var pages = 1280 - (emile + contes + ake) ;
	
	var vitesse = pages / temps ;
	
	document.getElementById("A-lire").innerHTML=pages ;
	document.getElementById("LireParJour").innerHTML=vitesse.toFixed(2) ;
	
}
