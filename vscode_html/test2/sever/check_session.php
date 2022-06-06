<?php
header("Content-type: text/html; charset=UTF-8");
$admin = false;

session_start();

if (isset($_SESSION["admin"]) && $_SESSION["admin"] === 1) {
    echo 1;
} else {
    echo 0;
}

?>