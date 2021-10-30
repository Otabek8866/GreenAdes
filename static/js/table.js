var data = {"first": {"0": ["Écully", "690810102", "Vianney", "1890.952158", "114", "127", "130", "101", "100", "129", "100"], "1": ["Criquetot-l'Esneval", "761960000", "Criquetot-l'Esneval", "2568", "90", "107", "68", "92", "103", "81", "99"], "2": ["Lavangeot", "392840000", "Lavangeot", "135", "124", "91", "197", "74", "92", "161", "86"], "3": ["Gap", "50610101", "Gap Centre", "2381.345487", "132", "99", "171", "213", "69", "147", "117"], "4": ["Warnécourt", "84980000", "Warnécourt", "366", "73", "125", "39", "63", "85", "67", "78"], "5": ["Grigny", "912860107", "La Grande Borne I", "3033.888395", "99", "57", "98", "106", "118", "85", "114"], "6": ["Busset", "30450000", "Busset", "940", "80", "94", "62", "67", "99", "73", "88"], "7": ["Mimizan", "401840102", "Plage", "1902.807094", "104", "98", "111", "78", "112", "107", "101"], "8": ["Tanay", "216190000", "Tanay", "233", "62", "107", "28", "74", "69", "54", "70"], "9": ["L'Isle-Adam", "953130105", "Le Haut de l'ISLE-Adam", "2803.179388", "100", "114", "85", "78", "119", "94", "105"]}, "second": {"10": ["Bahus-Soubiran", "400220000", "Bahus-Soubiran", "415", "82", "95", "69", "91", "85", "78", "87"], "11": ["Biaudos", "400440000", "Biaudos", "884", "73", "106", "51", "90", "68", "70", "76"], "12": ["Saulny", "576340000", "Saulny", "1389", "79", "135", "58", "69", "76", "84", "74"], "13": ["Jujols", "660900000", "Jujols", "44", "100", "0", "158", "102", "91", "105", "94"], "14": ["Bischheim", "670430102", "Est", "3284.020734", "113", "85", "144", "96", "104", "125", "101"], "15": ["Cachan", "940160111", "Grange-Ory Lumieres 2", "2874.245084", "111", "101", "105", "224", "67", "104", "119"], "16": ["Nicorps", "503760000", "Nicorps", "415", "78", "102", "53", "83", "90", "69", "88"], "17": ["Deux-Chaises", "30990000", "Deux-Chaises", "399", "87", "92", "61", "83", "112", "71", "103"], "18": ["Tresses", "335350000", "Tresses", "4557", "81", "115", "68", "89", "72", "84", "78"], "19": ["Villey-le-Sec", "545830000", "Villey-le-Sec", "411", "75", "120", "59", "112", "49", "80", "70"]}}

var current = {}
var previous = {};
var next = {};

var table = document.getElementById('main-table');
viewTable(current);
for (var key in data) {
    if (key == "first"){
        var current = data["first"];
        var next = data["second"];
        viewTable(current);
    }
}


function previousRows(){
    if (current.key == "1"){
    }
    else{
        deleteRows();
        next = current;
        current = previous;
        viewTable(current);
        previous = data;
    }
}

function nextRows(){
    if (current.key == "101"){
    }
    else{
        deleteRows();
        previous = current;
        current = next;
        viewTable(current);
        next = data;
    }
}

function deleteRows(){
    var elements = document.getElementsByClassName("to-be-deleted");
    while(elements.length > 0){
        elements[0].parentNode.removeChild(elements[0]);
    }
}

function viewTable(current) {
    var indexed = false;
    var id = 1;
    
    for (var key in current) {
        if (current.hasOwnProperty(key)) {
            if (indexed==false){
                id=key;
                indexed=true;
            }
            tr = table.insertRow(-1);
            tr.className += "to-be-deleted";

            for (var j = 0; j < current[key].length; j++) {
                var tabCell = tr.insertCell(-1);
                tabCell.innerHTML = current[key][j];
                if (j==0){tabCell.className += "sticky-col-1";}
                if (j==1){tabCell.className += "sticky-col-2";}
                if (j==2){tabCell.className += "sticky-col-3";}
            }
        }
    }
    document.getElementById('row-index').value = (parseInt(id) + 1) +" - "+(parseInt(id) + 10);
}

