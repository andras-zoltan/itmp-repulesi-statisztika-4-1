// lista elemek DINAMIC feltöltése
function listItemFeltolt() {
    
  sessionStorage.clear();  
    
  /* ---   próba adatok tömbben  -------*/
  var tomb=["HTML", "CSS", "JavaScript"];
  /* ---------------------------------- */

  var text="";
  var most="";
  var i;

  for (i = 0; i < tomb.length; i++) {
    
     /*-- itt link volt --
     text=text+"<a href=\"legitars.html\" class=\"list-group-item list-group-item-action\" id=\""+azon+"\">"+tomb[i]+"</a>";*/
    
     //-- de lecserélem buttonra --
     most=" type=\"button\" class=\"list-group-item list-group-item-action list-group-item-primary\" onclick=\"melyik(this)\">"+tomb[i]+"</button>";
    
     text=text+"<button"+most;

  };

document.getElementById("gombok").innerHTML=text;

}

// melyik légitársaság lett kiválasztva a listából? lista.html + paraméter-átadás
function melyik(elmnt) {
    var tartalom=elmnt.textContent;
    
    sessionStorage.setItem("data", tartalom);        //paraméter
    document.location ="../pages/legitars.html";
    
}

//teszt-hez képek cseréje
  var kepek = [];
  //kepek['HTML'] = 'figure-974810_640.jpg';
  kepek['HTML'] = 'logok/AS.JPG';
  kepek['CSS'] = 'logok/G4.JPG';
  kepek['JavaScript'] = 'logok/F9.JPG';

function mutatKep(oldal) {
    
    document.getElementById('logo').src = '../images/'+kepek[oldal];
    document.getElementById('logo').title = oldal;

}
//--- eddig tesztadat a légitárs logójával ;-)


// kiválasztott légitársaság nevét, képét frissíti a legitars.html oldalon
function mutat() {
    document.getElementById("data").innerHTML=sessionStorage.getItem("data");
    document.getElementById("neve").innerHTML=sessionStorage.getItem("data");
   
    mutatKep(sessionStorage.getItem("data"));
    
}

