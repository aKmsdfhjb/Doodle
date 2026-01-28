const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
let drawing = false;

ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);

canvas.addEventListener("mousedown", () => drawing = true);
canvas.addEventListener("mouseup", () => drawing = false);
canvas.addEventListener("mouseleave", () => drawing = false);

canvas.addEventListener("mousemove", draw);

function draw(event) {
    if (!drawing) return;

    ctx.fillStyle = "black";
    ctx.beginPath();
    ctx.arc(event.offsetX, event.offsetY, 8, 0, Math.PI * 2);
    ctx.fill();
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    document.getElementById("result").innerText = "Prediction: —";
}

function predict() {
    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append("image", blob);

        fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            document.getElementById("result").innerText =
                `Prediction: ${data.prediction} (${(data.confidence*100).toFixed(2)}%)`;
        });
    });
}
