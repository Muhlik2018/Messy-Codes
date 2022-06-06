<?php
header("Content-Type:application/json");
require_once("initial.php");
@$userAccount=$_REQUEST["userAccount"];
@$userPassword=$_REQUEST["userPassword"];
if($userAccount&&$userPassword){
    $sql="SELECT * FROM www_hcxdbwork_xy WHERE useAccount='$userAccount' and binary userPassword='$userPassword'";
    $result=mysqli_query($conn,$sql);
    $row=mysqli_fetch_row($result);
    if($row!=null)
    {
        session_start();
        $_SESSION["admin"]=$row[4];
        echo json_encode(["ok"=>1]);
    }
    else{
        echo json_encode(["ok"=>0,"msg"=>"用户名或密码不正确！"]);
    }
}