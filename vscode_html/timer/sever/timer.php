<?php
require_once("initial.php");
$round=$_REQUEST["round"];
$sql="insert into timer(round)values('$round')";
mysqli_query($conn,$sql);
$sql="select last_insert_id()";
$result=mysqli_query($conn,$sql);
$row=mysqli_fetch_row($result);
echo $row[0];
?>