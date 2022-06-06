<?php
require_once("initial.php");
$sql="SELECT * FROM user";
$result=mysqli_query($conn,$sql);
$json='';
while($row=mysqli_fetch_assoc($result)){
    $json.=json_encode($row).',';
}
$json =substr($json,0,-1);
echo '['.$json.']'

?>