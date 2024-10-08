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

    function uploadFile(file, fileType) {
        const formData = new FormData();
        formData.append('siteName', siteName);
        formData.append(fileType, file);  

        return fetch('http://0.0.0.0:8080/', { // Mude o endpoint para o ip do maquina que roda o server
            method: 'POST',
            body: formData,
            
        })
        .then(response => response.json())
        .then(data => {
            console.log(`Success uploading ${fileType}:`, data);
        })
        .catch(error => {
            console.error(`Error uploading ${fileType}:`, error);
        });
    }

    const uploadPromises = [];

    if (htmlFile) {
        uploadPromises.push(uploadFile(htmlFile, 'htmlFile'));
    }
    if (cssFile) {
        uploadPromises.push(uploadFile(cssFile, 'cssFile'));
    }
    if (jsFile) {
        uploadPromises.push(uploadFile(jsFile, 'jsFile'));
    }

    Promise.all(uploadPromises)
    .then(() => {
        console.log('All files uploaded successfully');
    })
    .catch((error) => {
        console.error('Error uploading files:', error);
    });
});
