<?php

//API Url
$data = file_get_contents('php://input');

$my_file = fopen("stock_transactions.json", "w") or die("Unable to open file!");

fwrite($my_file, $data);	
fclose($my_file);
//echo "File written successfully";

?>

def __str__(self):
        return f"Account {self.acc_id} owned by {self.owner} with balance {self.balance}"