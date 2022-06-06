<?php
$conn=mysqli_connect("localhost","timer","p2YnHRhB688DRxGE","timer");
if(mysqli_connect_errno($conn))
{
    echo "连接Mysql失败".mysqli_connect_error();
}
else{
    #echo "连接成功";
}

$sql="SET NAMES UTF8";
mysqli_query($conn,$sql);
?>
