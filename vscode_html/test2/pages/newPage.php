<!DOCTYPE html>
<html>
<body>

<?php
echo "我的第一段 PHP 脚本！";
?>

<?php
$conn=mysqli_connect("localhost","www_hcxdbwork_xy","3fxzAJL2fXk7LinS","www_hcxdbwork_xy");
if(mysqli_connect_errno($conn))
{
    echo "连接Mysql失败";
}
else
{
    echo "success!";
}

$result=mysqli_query($conn,"SELECT * FROM newUser WHERE userName='hcx'");

while($row =mysqli_fetch_array($result))
{
    echo $row['userAccount'];
}


?>


</body>
</html>