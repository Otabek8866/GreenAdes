function openShare() {
    document.getElementById("myForm").style.display = "block";
}

function closeShare() {
    document.getElementById("myForm").style.display = "none";
}

document.getElementById('export').addEventListener('click',exportPDF);

function exportPDF() {
    var sTable = document.getElementById('table-content').innerHTML;

    var style = "<style>";
    style = style + "table {width: 100%;font: 17px Calibri;}";
    style = style + "table, th, td {border: solid 1px #DDD; border-collapse: collapse;";
    style = style + "padding: 2px 3px;text-align: center;}";
    style = style + "</style>";

    var win = window.open('', '', 'height=700,width=700');

    win.document.write('<html><head>');
    win.document.write('<title>Profile</title>');
    win.document.write(style);
    win.document.write('</head>');
    win.document.write('<body>');
    win.document.write(sTable);
    win.document.write('</body></html>');

    win.document.close();

    win.print();
}