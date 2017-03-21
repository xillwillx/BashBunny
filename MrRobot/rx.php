<?php
date_default_timezone_set('Europe/Rome');
$file = $_SERVER['REMOTE_ADDR'] . "_" . date("Y-m-d_H-i-s") . ".txt";
file_put_contents($file, file_get_contents("php://input"));
?>