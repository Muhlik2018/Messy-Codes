<script src="../script/common.js"></script>
 function check_account(){
    var xhr=createXhr(); 
    var userAccount=$("userAccount").value;
    var url="../sever/check_name.php?userAccount="+userAccount;
    xhr.open("get",url,true);
    xhr.onreadystatechange=function(){
        if(xhr.readyState==4 && xhr.status==200){
        //判断状态，xhr请求状态为4，表示接收响应数据成功；当status的值是200的时候，表示服务器已经正确的处理请求以及给出响应
        $("uAccount-show").innerHTML=xhr.responseText;
        //提示内容
        };
    };

        //4.发送请求
        xhr.send(null);
        //get请求，参数写null
    }

//2.定义函数，判断两次密码是否一致
//当确认密码框失去焦点时，验证两次输入的密码是否一致，并给出提示（通过/密码不一致）
//给upwd 和 cpwd 加id
function check_password(){
    //1.获取两个密码框的值
    var userPassword=$("userPassword").value; 
    //$("upwd") 获取id值，函数在common.js中封装
    var checkPassword=$("checkPassword").value;
    if(userPassword==checkPassword && userPassword!=""){ 
    //判断是否相等，且密码不为空
        $("pwd-show").innerHTML="通过";  
        //提示到span中，用innerHTML
    }else{
        $("pwd-show").innerHTML="两次密码输入不一致";
    };
};