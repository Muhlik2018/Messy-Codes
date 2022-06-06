<?php
require_once("initial.php");
$aid=$_REQUEST["aid"];
$sql="DELETE FROM article WHERE aid='$aid'";
mysqli_query($conn,$sql);
?>