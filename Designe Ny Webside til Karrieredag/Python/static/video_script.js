var video = document.getElementById("webcam");
var canvas = document.getElementById("canvas");
var socket = new WebSocket('ws://localhost:5020/ws');

/*
function handleVideo() {
    navigator.mediaDevices.getUserMedia({
        video: true
    }).then(function (stream) {
        video.srcObject = stream;
        video.play();
    });
}
*/
video.addEventListener('loadedmetadata', function () {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
});

setInterval(function(){
    var ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    var imgData = canvas.toDataURL("image/jpeg");
    socket.send(imgData);
},200);

