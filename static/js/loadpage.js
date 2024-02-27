function loadPage(pageName) {
    document.getElementById("content").innerHTML = "";
    fetch(pageName)
    .then(response => response.text())
    .then(data => {
        document.getElementById("content").innerHTML = data;
    });
}
