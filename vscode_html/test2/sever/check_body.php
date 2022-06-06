<?php

  require("initial.php");


  $aid=$_REQUEST["aid"];

  session_start();
  $sql="SELECT * FROM article WHERE aid='$aid'";
  $reply="SELECT * FROM reply WHERE aid='$aid'"
  $result=mysqli_query($conn,$sql);
  $result2=mysqli_query($conn,$reply);
  $row=mysqli_fetch_row($result);
  if($row!=null){
    $header=<<<Header
    
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8"> 
    <title>密斯卡托尼克大学</title> 
    
    <link rel="stylesheet" type="text/css" href="../style/standard.css" />

    <script src="https://code.jquery.com/jquery-2.2.3.js" type="text/javascript">
</script>
<script>
$(document).ready(function(){
	$("#btn").click(function(){
		var abody=$("#body").val();
		var cbody=$.trim(abody);
		console.log(abody);
		if(cbody!=""){
		$.post("sever/reply.php",
		{
        aid:$aid,
        body:abody
    },
		function(data){
			if(data==1){
				alert("发布成功");
				location.reload();
			}
			else
				alert("发布失败,请先登陆");
		});}
		else if(cbody==""){
			alert("请写内容");
		}	
	});
});
</script>












    
    </head>
    
    <body>
    <div id="begin"> 
        <a href="http://www.hcxdbwork.xyz"><img src="../pictures/logo.png">
        </a>
    </div>
    
    <div id="recommend">
        <p>
            今日推荐：
            <a class="nodecorate" href="https://www.decembertwentytwo.com/index.php/2020/02/19/pikapika/">
                <s>恰饭</s><b>PikaPika~</b>
            </a>
        </p>
    </div>
    
    
    <div id="article">
    
    <h1 style="border-top-style:solid;border-top-color: #4169E1">
Header;
   
  
$endHeader=<<<Endheader
</h1>
<p style="border-bottom-style:solid;border-bottom-color: #4169E1">
Endheader;


$last=<<<last
</p>

<label>回复</label>
<textarea rows="10"
cols="30"
id="body">
</textarea>
<br>
<button id="btn">
点击提交
</button>

</div>

<div id="end">
    <h>      
        <a href="beian.miit.gov.cn">
            beian.miit.gov.cn
        </a>
        <h>
            赣ICP备20000365号<br>
        </h>
    </h>
        <h>
            <b>是胡辰昕做的网页哦</b>
        </h>


</div>

</body>
</html>

last;

echo $header;
echo $row[2];
echo $endHeader;
echo "by: <b>";
echo $row[6];
echo "</b> at ";
echo $row[1];
echo"<br><br>";
echo $row[3];
while($row2=mysqli_fetch_assoc($result2)){
    echo"<p>";
    echo " by <b>";
    echo $row2[2];
    echo"at </b>";
    echo"row[1]";
    echo" : ";
    echo $row[3];
    echo"</p>";
}

echo $last;


  }
  
  
  
  
  
  else{
    echo "失败";
  };
  ?>