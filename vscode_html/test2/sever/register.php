<?php

    $userName=$_REQUEST["userName"];
    $userAccount=$_REQUEST["userAccount"];
    $userPassword=$_REQUEST["userPassword"];
    $userTrueName=$_REQUEST["userTrueName"];

    require("initial.php");
    $sql="SELECT * FROM newUser where userAccount='$userAccount'";
    $result=mysqli_query($conn,$sql);
    $row=mysqli_fetch_row($result);
    if($row==NULL){
        $sql="SELECT * FROM user where userAccount='$userAccount'";
        $result=mysqli_query($conn,$sql);
        $row=mysqli_fetch_row($result);
        if($row==NULL){
            $sql="insert into newUser(userName,userAccount,userPassword,userTrueName)values('$userName','$userAccount','$userPassword','$userTrueName')";
            $result=mysqli_query($conn,$sql);
            if($result==true) 
            {                        
                echo "注册成功";
                session_start();
                $_SESSION["reg"]=1;
            }
            
            else{
                echo "注册失败：系统故障";
            };
        }
        else
        {
            echo "注册失败：已注册";
        }
    }
    else
        echo "注册失败：已经提交注册申请";



  