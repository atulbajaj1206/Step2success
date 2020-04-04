$(function() {
    
 
    $('#rtpa').click(function() {
        
      
        $.ajax({
            url : '/api' ,
            success: function(data) {
                $('#current_time').html(data['current_time'] );
                  $('#time').html(data['time'] );
                    
                     

                 
                 
            }
        });
    });

})