<?php
header("Content-type: text/html; charset=UTF-8");
session_start();
$number=$_SESSION["number"];

$header1=<<<Header
<!DOCTYPE html>
<html>
<head>
	
<meta charset="utf-8"> 
<title>华工计时器</title>

<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
<script src="https://code.jquery.com/jquery-2.2.3.js" type="text/javascript">
</script>


</head>
<body style="background-color:
#FAEBD7">
	<div style="
	background-color:#B22222;
	height:150px;">
	<a href="http://www.hcxdbwork.xyz"><img src="../picture/logo.png">
    </a>
	</div>
	<div style="height:600;
	text-align:center;" 
	id="main">
Header;
$header2=<<<Header2
</div>

<div style="height:600;
text-align:center;" >
<button type="button" class="btn btn-primary" id="confirm">提交</button>

<script type="text/javascript">

    $(document).ready(function(){
        $('#confirm').click(function(){
            for(var i=0;i<
Header2;
$body=<<<BODY 
;i++){
    var name='name'+i;
    console.log(name);
    console.log($('#name').html());
    var p_min='p_min'+i;
    var p_sec='p_sec'+i;
    var n_min='n_min'+i;
    var n_sec='n_sec'+i;
    if($('#name').val()==''||$('p_min').val()==''||$('#p_sec').val()==''||$('#n_min').val()==''||$('#n_sec').val()=='')
    {	
        alert("有地方没填哦");
        location.reload();
    }
}
alert("成功");
});

});
</script>


</div>
</body>
</html>
BODY;
echo $header1;
for ($x=0; $x<$number; $x++) {
  echo "数字是：$x <br>";
  echo'<h3>环节 ';
  echo $number;
  echo'</h3>';
  echo'<div><p>环节名称：<input type="text" id="name';
  echo $number;
  echo'" size=20></p><br></div>';
  echo'<div><p>正方时间：<input type="text" id="p_min';
  echo $number;
  echo'" size=20>分</p>';
  echo'<p>正方时间：<input type="text" id="p_sec';
  echo $number;
  echo'" size=20>秒</p><br></div>';
  echo'<div><p>反方时间：<input type="text" id="n_min';
  echo $number;
  echo'" size=20>分</p>';
  echo'<p>反方时间：<input type="text" id="n_sec';
  echo $number;
  echo'" size=20>秒</p><br></div>';
} 
echo $header2;
echo $number;
echo $body;





?>