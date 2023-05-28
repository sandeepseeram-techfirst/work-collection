<?php

//API Url
$data = file_get_contents('php://input');

$my_file = fopen("stocks.json", "w") or die("Unable to open file!");


?>