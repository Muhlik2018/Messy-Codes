<?php
require_once("initial.php");
session_start();
$userAccount=$_SESSION["account"];
$userName=$_REQUEST["userName"];
$sql="UPDATE user SET userName='$userName' where userAccount='$userAccount'";
$result=mysqli_query($conn,$sql);
$row=mysqli_fetch_row($result);
$_SESSION["account"]=$userName;

?>