document.getElementById("submit-btn").addEventListener("click", function() {
  const siteName = document.getElementById("site-name").value;
  const htmlFile = document.getElementById("html-upload").files[0];
  const cssFile = document.getElementById("css-upload").files[0];
  const jsFile = document.getElementById("js-upload").files[0];

  if (!siteName) {
      alert("Por favor, insira o nome do site.");
      return;
  }

  // Verificação
  if (!htmlFile) {
      alert("Por favor, selecione um arquivo HTML.");
      return;
  }

  if (!cssFile) {
      alert("Por favor, selecione um arquivo CSS.");
      return;
  }

  if (!jsFile) {
      alert("Por favor, selecione um arquivo JavaScript.");
      return;
  }

  alert(`Nome do site: ${siteName}\nArquivos selecionados:\nHTML: ${htmlFile.name}\nCSS: ${cssFile.name}\nJavaScript: ${jsFile.name}`);
});

document.getElementById('submit-btn').addEventListener('click', function() {
  
    const siteName = document.getElementById('site-name').value;
    const htmlFile = document.getElementById('html-upload').files[0];
    const cssFile = document.getElementById('css-upload').files[0];
    const jsFile = document.getElementById('js-upload').files[0];

    const formData = new FormData();
    formData.append('siteName', siteName);
    if (htmlFile) {
        formData.append('htmlFile', htmlFile);
    }
    if (cssFile) {
        formData.append('cssFile', cssFile);
    }
    if (jsFile) {
        formData.append('jsFile', jsFile);
    }

    fetch('http:localhost:8080/', { 
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});