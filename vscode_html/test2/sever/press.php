<?php
    $head=$_REQUEST["head"];
    $body=$_REQUEST["body"];
    session_start();
    $userAccount=$_SESSION["account"];
    require("initial.php");

    $sql="insert into article(head,body,userAccount)values('$head','$body','$userAccount')";
    $result=mysqli_query($conn,$sql);
    if($result==true){                        
        echo 1;
    }else{
        echo 0;
    };
?>