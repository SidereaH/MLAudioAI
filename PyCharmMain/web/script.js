const fileInput =

function reinitFiles() {
    eel.reinitFiles()
}
function addLearnMach(){
    eel.addLearnMach()
}
function audioProccessing(path){
    eel.audioProcjs(path)
}

let inputPath = document.getElementById('audioPath')
const btn = document.getElementById('btn3')
btn3.onclick = function() {
    console.log(inputPath.value)
    eel.audioProcjs(inputPath.value)
}

