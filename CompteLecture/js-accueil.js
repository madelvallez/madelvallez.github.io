function resu() {
	var emile = parseInt(document.getElementById("stadeEmile").value);
	var contes = parseInt(document.getElementById("stadeAndersen").value);
	var ake = parseInt(document.getElementById("stadeAke").value);
	var date = document.getElementById("jour").valueAsDate;
	
	var date_fin = new Date("2021-08-29");
	var diff = date_fin.getTime() - date.getTime();
	var temps = diff / (1000 * 3600 * 24); 
	
	var pages = 1280 - (emile + contes + ake) ;
	
	var vitesse = pages / temps ;
	
	document.getElementById("A-lire").innerHTML=pages ;
	document.getElementById("LireParJour").innerHTML=vitesse ;
	
}