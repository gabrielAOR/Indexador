const url = "http://0.0.0.0:8080/"

document.getElementById("submit-btn").addEventListener("click", function() {
    const siteName = document.getElementById("site-name").value;
    const htmlFile = document.getElementById("html-upload").files[0];
    const cssFile = document.getElementById("css-upload").files[0];
    const jsFile = document.getElementById("js-upload").files[0];

    if (!siteName) {
        alert("Por favor, insira o nome do site.");
        return;
    }

    if (!htmlFile) {
        alert("Por favor, selecione um arquivo HTML.");
        return;
    }

    alert(`Arquivos enviados site acessivel na rota: ${url}${siteName}`)

    function uploadFile(file, fileType) {
        const formData = new FormData();
        formData.append('siteName', siteName);
        formData.append(fileType, file);  

        return fetch(url, {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            console.log(`Success ${fileType}:`, data);
        })
        .catch(error => {
            console.error(`Error ${fileType}:`, error);
        });
    }

    const uploadPromises = [];

    uploadPromises.push(uploadFile(htmlFile, 'htmlFile'));

    if (cssFile) {
        uploadPromises.push(uploadFile(cssFile, 'cssFile'));
    }

    if (jsFile) {
        uploadPromises.push(uploadFile(jsFile, 'jsFile'));
    }

    Promise.all(uploadPromises)
    .then(() => {
        console.log('Todos os arquivos foram salvos');
    })
    .catch((error) => { 
        console.error('Error:', error);
    });
});
