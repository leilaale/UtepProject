const dragArea = document.querySelector('.drop-zone');
const dragText = document.querySelector('.drop_prompt');

let button = document.querySelector('.uploadButton');
let input = document.querySelector('input');

button.onclick = () => {
    input.click();
}

input.addEventListener('change', function () {
    file = this.files;
    dragArea.classList.add('active');
    displayFile();

});


let file; 

dragArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dragText.textContent = 'Release to Upload';
    dragArea.classList.add('active');
    console.log('File is inside the Drag Area');
})

dragArea.addEventListener('dragleave', () => {
    dragText.textContent = "Drag & Drop";
    dragArea.classList.remove('active');

    //console.log("File left Drag Area");
})

dragArea.addEventListener('drop', (event) => {
    event.preventDefault();
    file = event.dataTransfer.files;
    console.log(file);
    
    displayFile()

    //console.log("The File is dropped in Drag Area");
})


function displayFile(){
    let fileType = file.type;
    console.log(fileType);

    let validExtensions = ['application/pdf']

    if(validExtensions.includes(fileType)) {
        let fileReader = new FileReader();
        fileReader.onload = () => {
            let fileURL = fileReader.result;
        };
        fileReader.readAsDataURL(file);
    
    } else {
        alert('This file is not supported');
        dragArea.classList.remove('active');
    }
}

