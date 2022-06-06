<?php
require_once("initial.php");
mysqli_set_charset($mysqli, "utf8"); 
$sql="SELECT * FROM newUser";
$result=mysqli_query($conn,$sql);
$json='';
while($row=mysqli_fetech_assoc($result)){
    $json.=json_encode($row).',';
}
$json =substr($json,0,-1);
echo '['.$json.']'

?>