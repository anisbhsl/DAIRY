

    //initialize the map
    (function initMap(){
    var loc={lat: 27.7172, lng:85.3240};
    var map = new google.maps.Map(
                    document.getElementById('map'), {zoom: 12, center: loc});
    /*

    var iw=new google.maps.InfoWindow();

    //parse station.json file
    (function parseJson(){
        var request=new XMLHttpRequest(); //make a request
        request.open('GET','/dashboard/static/json/station.json',true);  //open via get url request
        //parse and work with our data
        request.onload=function(){
            data=JSON.parse(this.response); //parse into data object
            for(var i=0;i<data.length;i++){


                //initialize the map with markers

                loc1 = {lat: data[i].lat, lng: data[i].long};


                marker = new google.maps.Marker({position: loc1, map: map});
                //add event listener

                console.log(data[i].station_name+'');



                //add event listener using callback function
                google.maps.event.addListener(marker,'click',(function(marker,i) {
                        return function () {
                            var w=document.getElementById("station-details")
                                w.innerHTML="id: "+data[i].station_id+"<br>"+ data[i].station_name+"<br>"+"Latitude:"+
                                    data[i].lat+"<br>"+"Longitude:"+data[i].long;
                            iw.setContent(data[i].station_name);
                            iw.open(map, marker);
                        }
                    }
                )(marker,i));
            }
        }
        request.send();
    })(); //parseJSON call
    */
    })();  //initMap










