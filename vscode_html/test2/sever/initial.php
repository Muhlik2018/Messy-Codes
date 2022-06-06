<?php
$conn=mysqli_connect("localhost","www_hcxdbwork_xy","3fxzAJL2fXk7LinS","www_hcxdbwork_xy");
if(mysqli_connect_errno($conn))
{
    echo "连接Mysql失败".mysqli_connect_error();
}
else{
    echo "连接成功";
}

$sql="SET NAMES UTF8";
mysqli_query($conn,$sql)



