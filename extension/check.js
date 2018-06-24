const jsdom = require("jsdom");
const window = jsdom.jsdom().defaultView;

var formData = new FormData();
formData.append("name", t);

var xhr = new XMLHttpRequest();  
xhr.open("POST", "https://nameless-fjord-34984.herokuapp.com/");
xhr.onload = function(event){ 
    console.log('YEAS');
    console.log("The server responded with: " + event.target.response); 
}; 
xhr.send(formData);