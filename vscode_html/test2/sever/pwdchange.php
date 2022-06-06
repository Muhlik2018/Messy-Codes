<?php
require_once("initial.php");
session_start();
$userAccount=$_SESSION["account"];
$userPassword=$_REQUEST["userPassword"];
$sql="UPDATE user SET userPassword='$userPassword' where userAccount='$userAccount'";
$result=mysqli_query($conn,$sql);
$row=mysqli_fetch_row($result);

?>