function GetResults() {
  var keyword = document.getElementById('keyword').value;
  var url = "/search/" + keyword;

  var xhr = new XMLHttpRequest();
  xhr.open("GET", url, true);
  xhr.onload = function(e) {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        var json = JSON.parse(xhr.responseText);
        console.log(json);
        if (json.results.length > 0) {
          resetBody(json);
        } else {
          alert("未找到");
        }
      } else {
        console.error(xhr.statusText);
      }
    }
  };
  xhr.onerror = function(e) {
    console.error(xhr.statusText);
  };
  xhr.send(null);
}

function resetBody(json) {
  htmlSnippet = '';

  for (var i = 0; i < json.results.length; i++) {
    htmlSnippet += '<img style="margin-top: 5px;" width="144px" height="160px" src="' + json.results[i][2] + '" alt="' + json.results[i][1] +'" class="img-rounded">&nbsp&nbsp'
  }

  document.getElementById('booklist').innerHTML = htmlSnippet;
}
