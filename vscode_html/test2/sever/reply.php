<?php
    $aid=$_REQUEST["aid"];
    $body=$_REQUEST["body"];
    session_start();
    $userAccount=$_SESSION["account"];
    require("initial.php");

    $sql="insert into reply(aid,body,userAccount)values('$aid','$body','$userAccount')";
    $result=mysqli_query($conn,$sql);
    if($result==true){                        
        echo 1;
    }else{
        echo 0;
    };
?>