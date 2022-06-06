<?php
require_once("initial.php");
session_start();
$userAccount=$_SESSION["account"];
$sql="SELECT * FROM article where userAccount='$userAccount";
$result=mysqli_query($conn,$sql);
$json='';
while($row=mysqli_fetch_assoc($result)){
    $json.=json_encode($row).',';
}
$json =substr($json,0,-1);
echo '['.$json.']'

?>