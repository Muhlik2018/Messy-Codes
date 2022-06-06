<?php
require_once("initial.php");
$userAccount=$_REQUEST["userAccount"];
$sql="UPDATE user SET level=1 WHERE userAccount='$userAccount'";
mysqli_query($conn,$sql) or die ('删除数据出错');
?>