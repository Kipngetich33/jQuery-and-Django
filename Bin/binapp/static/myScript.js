var collected_data = []


function get_data(){
    $.ajax({
        type:'GET',
        url: '/home/',
        dataType : 'json',
        cache: false,
        success: function(data) {
            // posting()
            my_data = data
            my_data.forEach(function(obj) { console.log(obj.id); });
        },
        error:function(){ 

        }
    });

}

function posting(){

    $.ajax({
        type:'POST',
        url: '/third/',
        dataType : 'json',
        cache: false,
        success: function(data) {
            console.log("succefully posted")
        },
        error:function(){
            console.log("Unable to Post") 
        }
    });

}

// document ready function
$( document ).ready(function() {
    console.log( "ready!");
    get_data() 

});

