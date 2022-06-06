<?php	
	require_once("initial.php");
	$identity=$_REQUEST["identity"];
    session_start();
    $sql="select * from timer where id='$identity'";
    $result=mysqli_query($conn,$sql);
    $row=mysqli_fetch_row($result);
	if($row!=null)
    {
    	$_SESSION["identity"]=$identity;
    	$_SESSION["tot_p"]=$row[1];
    	$_SESSION["cur_p"]=0;
    	echo 0;
    }
    else
    echo 1;
?>