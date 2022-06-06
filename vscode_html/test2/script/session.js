<script src="https://code.jquery.com/jquery-2.2.3.js" type="text/javascript">
</script>
$(document).ready(function(){
    $("#btn").click(function(){
        $.get(
            "sever/check_session.php",
            function(data)
            {
                if(data==2)
                {
                    alert(data);
                    $("#first").text("管理员页面");
                    $("#first").attr("href","pages/manager.html")
                }
                else if(data==1)
                {
                    alert(data);
                    $("#first").text("用户页面");
                    $("#first").attr("href","pages/user.html")
                }
            });
    });
    
});