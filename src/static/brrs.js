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
    htmlSnippet += '<img src="' + json.results[i].image + '" alt="..." class="img-rounded">'
  }

  document.getElementById('booklist').innerHTML = htmlSnippet;
}
