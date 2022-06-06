<?php
require_once("initial.php");
$id=$_REQUEST["id"];
$name=$_REQUEST["name"];
$number=$_REQUEST["number"];
$p_min=$_REQUEST["p_min"];
$p_sec=$_REQUEST["p_sec"];
$n_min=$_REQUEST["n_min"];
$n_sec=$_REQUEST["n_sec"];

$sql="insert into round(id,name,number,p_min,p_sec,n_min,n_sec)values('$id','$name','$number','$p_min','$p_sec','$n_min','$n_sec')";
mysqli_query($conn,$sql) or die("加入失败");
?>