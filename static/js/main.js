// https://www.codegrepper.com/code-examples/html/html+filter+table+multiple+columns
function filterTable() {
    // Declare variables
  var input, filter, table, tr, td, i;
  input = document.getElementById("SearchInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("searchableTable");
  var rows = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
  for (i = 1; i < rows.length; i++) {
    var cells = rows[i].getElementsByTagName("td");
    var j;
    var rowContainsFilter = false;
    for (j = 0; j < cells.length; j++) {
      if (cells[j]) {
        if (cells[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
          rowContainsFilter = true;
          continue;
        }
      }
    }

    if (! rowContainsFilter) {
      rows[i].style.display = "none";
    } else {
      rows[i].style.display = "";
    }
  }
}