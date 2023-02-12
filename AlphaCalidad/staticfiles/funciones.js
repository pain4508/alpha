// funciones formulario chile mini en campo




function kgApro() {
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");

    for ( i = 0; i < rows.length; i++) {

        let r = [];
        if(dato1 = rows[i].cells[5]){
            dato1 = rows[i].cells[5].innerHTML;   
            dato2 = rows[i].cells[10].innerHTML;
            rows[i].cells[8].innerHTML = (parseFloat(dato1) - parseFloat(dato2)).toFixed(2);
    
  }
}
}

function porcApro() {
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");

    for ( i = 0; i < rows.length; i++) {

        let r = [];
        if(dato1 = rows[i].cells[8]){
            dato1 = rows[i].cells[8].innerHTML;   
            dato2 = rows[i].cells[5].innerHTML;
            rows[i].cells[9].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
  }
}
}

function porcRech() {
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");

    for ( i = 0; i < rows.length; i++) {

        let r = [];
        if(dato1 = rows[i].cells[10]){
            dato1 = rows[i].cells[10].innerHTML;   
            dato2 = rows[i].cells[5].innerHTML;
            rows[i].cells[11].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
  }
}
}


function relacionCaja5() {
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");

    for ( i = 0; i < rows.length; i++) {

        let r = [];
        if(dato1 = rows[i].cells[8]){
            dato1 = rows[i].cells[8].innerHTML;   
            dato2 = rows[i].cells[6].innerHTML;
            rows[i].cells[12].innerHTML = ((parseFloat(dato1) / 5) / (parseFloat(dato2))).toFixed(2);
    
  }
}
}


function sumaKgRechazo(){
    let tabla = document.getElementById("body1");
    let fila = tabla.getElementsByTagName("tr");

    

    for (let j= 0; j < fila.length; j++) {
        
        let r = [];
       if(dato1 = fila[j].cells[13]){
        dato1 = fila[j].cells[13].innerHTML;
       dato2 = fila[j].cells[15].innerHTML;
       dato3 = fila[j].cells[17].innerHTML;
       dato4 = fila[j].cells[19].innerHTML;
       dato5 = fila[j].cells[21].innerHTML;
       dato6 = fila[j].cells[23].innerHTML;
       dato7 = fila[j].cells[25].innerHTML;
       dato8 = fila[j].cells[27].innerHTML;
       dato9 = fila[j].cells[29].innerHTML;
       dato10 = fila[j].cells[31].innerHTML;
       dato11 = fila[j].cells[33].innerHTML;
       dato12 = fila[j].cells[35].innerHTML;
       dato13 = fila[j].cells[37].innerHTML;
       dato14 = fila[j].cells[39].innerHTML;

            fila[j].cells[10].innerHTML = (parseFloat(dato1) + parseFloat(dato2) + parseFloat(dato3) + parseFloat(dato4) + parseFloat(dato5) + parseFloat(dato6) + parseFloat(dato7) + parseFloat(dato8) + parseFloat(dato9) + parseFloat(dato10) + parseFloat(dato11) + parseFloat(dato12) + parseFloat(dato13) + parseFloat(dato14)).toFixed(2);
        }
    }
}


function KgCaja(){
  let table = document.getElementById("body1");
  let rows = table.getElementsByTagName("tr");

  for ( i = 0; i < rows.length; i++) {

    let r = [];
    if(dato1 = rows[i].cells[5]){
     dato1 = rows[i].cells[5].innerHTML;   
     dato2 = rows[i].cells[6].innerHTML;
     
    rows[i].cells[7].innerHTML = parseFloat(dato1) / parseFloat(dato2).toFixed(2);

  }

}
}

// funciones de daños---------------------------------------------------
function calizDañado(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[13]){
       dato1 = rows[i].cells[13].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[14].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
   
    }
  }
}

function Mecanico(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[15]){
       dato1 = rows[i].cells[15].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[16].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}

function Gusano(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[17]){
       dato1 = rows[i].cells[17].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[18].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}

function GOptimo(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[19]){
       dato1 = rows[i].cells[19].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[20].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}

function Silverado(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[21]){
       dato1 = rows[i].cells[21].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[22].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}

function MateriaExtraña(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[23]){
       dato1 = rows[i].cells[23].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[24].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}

function SobreMaduro(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[25]){
       dato1 = rows[i].cells[25].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[26].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}

function Blossom(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[27]){
       dato1 = rows[i].cells[27].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[28].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}

function Cracking(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[29]){
       dato1 = rows[i].cells[29].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[30].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}

function Deforme(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[31]){
       dato1 = rows[i].cells[31].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[32].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}

function Flacido(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[33]){
       dato1 = rows[i].cells[33].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[34].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}

function Hongo(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[35]){
       dato1 = rows[i].cells[35].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[36].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}

function Podrido(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[37]){
       dato1 = rows[i].cells[37].innerHTML;   
       dato2 = rows[i].cells[10].innerHTML;
      rows[i].cells[38].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}

function Tamaño(){
    let table = document.getElementById("body1");
    let rows = table.getElementsByTagName("tr");
  
    for ( i = 0; i < rows.length; i++) {
  
      let r = [];
      if(dato1 = rows[i].cells[39]){
       dato1 = rows[i].cells[39].innerHTML;   
       dato2 = rows[i].cells[12].innerHTML;
      rows[i].cells[40].innerHTML = ((parseFloat(dato1) / parseFloat(dato2)) * 100).toFixed(2);
    
    }
  }
}


// se declaran las funciones para que se muestren al iniciar la pagina.
KgCaja();
sumaKgRechazo();
kgApro();
porcApro();
porcRech();
relacionCaja5();
calizDañado();
Mecanico();
Gusano();
GOptimo();
Silverado();
MateriaExtraña();
SobreMaduro();
Blossom();
Cracking();
Deforme();
Flacido();
Hongo();
Podrido();
Tamaño();

//Funcion Totales

function sumaKg(){
  var dato1 = 0;
  var table = document.getElementById("body1");
  var rows = table.getElementsByTagName("tr");

  for ( var i = 0; i < rows.length; i++) {

    if(rows[i].cells[5]){
     dato1 += Number(rows[i].cells[5].innerHTML);      
     console.log(dato1);
     document.getElementById("sumaKg").innerHTML = dato1.toFixed(2);
    }

}

}

function sumaKCajaCosechas(){
  var dato1 = 0;
  var table = document.getElementById("body1");
  var rows = table.getElementsByTagName("tr");

  for ( var i = 0; i < rows.length; i++) {

    if(rows[i].cells[6]){
     dato1 += Number(rows[i].cells[6].innerHTML);   
     document.getElementById("sumaCajaCosechas").innerHTML = dato1.toFixed(2);
    }

}

}

function divisionkgCaja(){
  let dato1 = document.getElementById("sumaKg").innerHTML;
  let dato2 = document.getElementById("sumaCajaCosechas").innerHTML;

  resultado = parseFloat(dato1) / parseFloat(dato2);

  document.getElementById("sumakgcaja").innerHTML = resultado.toFixed(2);
}

//sumaKg();
sumaKCajaCosechas();
divisionkgCaja();

//filtro por codigo
function buscarCodigo() {
  // Declare variables 
  var input, filter, table, tr, td, i, j, visible;
  input = document.getElementById("txtFiltro");
  filter = input.value.toUpperCase();
  table = document.getElementById("body1");
  tr = table.getElementsByTagName("tr");
  dato1 = 0


  // Funcion buscar
  for (i = 0; i < tr.length; i++) {
    visible = false;

     

    /* Obtenemos todas las celdas de la fila, no sólo la primera */
    td = tr[i].getElementsByTagName("td");
    for (j = 0; j < td.length; j++) {
      if (td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
        visible = true;
        dato1 += Number(tr[i].cells[5].innerHTML);      
        console.log(dato1);

        
    }
    document.getElementById("sumaKg").innerHTML = dato1.toFixed(2);
    }

    
    if (visible === true) {
      tr[i].style.display = "";
      
    } else {
      tr[i].style.display = "none";
    }
  }
 

}

var descargaExcel = (function() {
  var uri = 'data:application/vnd.ms-excel;base64,'
    , template = '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40"><head><!--[if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>{worksheet}</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]--><meta charset="utf-8"></meta></head><body><table>{table}</table></body></html>'
    , base64 = function(s) { return window.btoa(unescape(encodeURIComponent(s))) }
    , format = function(s, c) { return s.replace(/{(\w+)}/g, function(m, p) { return c[p]; }) }
  return function(table, name) {
    if (!table.nodeType) table = document.getElementById(table) 
    var ctx = {worksheet: name || 'Registro Nuevo', table: table.innerHTML}
    window.location.href = uri + base64(format(template, ctx))
  }
})()

