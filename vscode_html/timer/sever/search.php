<?php
session_start();
$identity=$_SESSION["identity"];
require_once("initial.php");
$round=$_REQUEST["timer"];
$sql="select * from round where id='$identity'";

$result=mysqli_query($conn,$sql);
$json='';
while($row=mysqli_fetch_assoc($result)){
    $json.=json_encode($row).',';
}
$json =substr($json,0,-1);
echo '['.$json.']'


?>