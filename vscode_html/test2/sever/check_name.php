<?php

  require("initial.php");

  $userAccount=$_REQUEST["userAccount"];


  $sql="SELECT * FROM user userAccount='$userAccount'";
  $result=mysqli_query($conn,$sql);

  $row=mysqli_fetch_row($result);
  if($row==null){
    echo "通过";
  }else{
    echo "用户名称已存在";
  };