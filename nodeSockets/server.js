var request = require('request');
var express = require('express');
var app = express();
var io = require('socket.io');
var serv_io = io.listen(3300);

app.use(express.static(__dirname + '/public'));

setInterval(function(){
    request("http://data.sparkfun.com/output/9JQorAyYQ9TpLDg3n6Wl.json", function(error, response, body) {
      //console.log(body);
      var rawData = JSON.parse(body);
      var dust = rawData[0].dust;
      var humidity = rawData[0].humidity;
      var temp = rawData[0].temp;
      console.log("Dust Value: " + dust);
      console.log("Humidity Value: " + humidity);
      console.log("Temp Value: " + temp);
      serv_io.emit('sensor1', dust);
  });
},5000);


console.log("Server running on port: 3000");
app.listen(3000);
