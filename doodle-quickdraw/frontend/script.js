const canvas=document.getElementById("canvas");
const ctx=canvas.getContext("2d");
const statusNode=document.getElementById("status");
let drawing=false;
let hasInk=false;
function resetCanvas(){ctx.fillStyle="#fff";ctx.fillRect(0,0,canvas.width,canvas.height);ctx.lineWidth=12;ctx.lineCap="round";ctx.lineJoin="round";hasInk=false;document.getElementById("prediction").textContent="—";document.getElementById("confidence").textContent="No result yet";statusNode.textContent="Canvas cleared."}
function point(event){const rect=canvas.getBoundingClientRect();return{x:(event.clientX-rect.left)*canvas.width/rect.width,y:(event.clientY-rect.top)*canvas.height/rect.height}}
canvas.addEventListener("pointerdown",event=>{event.preventDefault();drawing=true;canvas.setPointerCapture(event.pointerId);const p=point(event);ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.lineTo(p.x+.1,p.y+.1);ctx.stroke();hasInk=true});
canvas.addEventListener("pointermove",event=>{if(!drawing)return;const p=point(event);ctx.strokeStyle="#111";ctx.lineTo(p.x,p.y);ctx.stroke()});
function stop(){drawing=false;ctx.beginPath()}
canvas.addEventListener("pointerup",stop);canvas.addEventListener("pointercancel",stop);canvas.addEventListener("lostpointercapture",stop);
document.getElementById("clear").addEventListener("click",resetCanvas);
document.getElementById("predict").addEventListener("click",()=>{const api=document.getElementById("apiUrl").value.trim().replace(/\/$/,"");if(!hasInk){statusNode.textContent="Draw something before requesting a prediction.";return}if(!api){statusNode.textContent="Enter the URL of a running Flask API. GitHub Pages cannot run the Python model.";return}canvas.toBlob(async blob=>{if(!blob){statusNode.textContent="Could not export the drawing.";return}const form=new FormData();form.append("image",blob,"sketch.png");statusNode.textContent="Sending drawing to the model…";const button=document.getElementById("predict");button.disabled=true;try{const response=await fetch(api+"/predict",{method:"POST",body:form});const data=await response.json();if(!response.ok)throw new Error(data.error||"Prediction request failed");document.getElementById("prediction").textContent=data.prediction;document.getElementById("confidence").textContent=(Number(data.confidence)*100).toFixed(1)+"% model score";statusNode.textContent="Inference complete."}catch(error){statusNode.textContent="Could not reach the API: "+error.message}finally{button.disabled=false}},"image/png")});
resetCanvas();