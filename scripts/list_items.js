

/* ---   próba adatok   --------------*/
var tomb=["HTML", "CSS", "JavaScript"];
/* ---------------------------------- */

var text="";
var i;

for (i = 0; i < tomb.length; i++) {
    
    /*text=text+"<li>"+tomb[i]+"</li>";    ha sima lista lenne*/
    /*                                     de nem az, hanem list-group */
    /* -- itt be kell majd állítani, hogy melyik légitársaság */
    text=text+"<a href=\"legitars.html\" class=\"list-group-item list-group-item-action\">"+tomb[i]+"</a>";
    
}

document.getElementById("ujak").innerHTML=text;