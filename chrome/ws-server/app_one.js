var hybridge_id = "cjgpdcodlpoonjhgljcikndlgodgpdfb";
var port = null;

window.onload = function window_onload() {
    port = chrome.runtime.connect(hybridge_id, {name: "app_one"});
    port.onMessage.addListener(function(msg) {
        document.getElementById("arg-a").innerHTML = msg.a;
        document.getElementById("arg-b").innerHTML = msg.b;
        
        console.log("client app_one received:");
        console.log(msg); 
    });
}

