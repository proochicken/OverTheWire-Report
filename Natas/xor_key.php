<?php
    $defaultdata = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));

    echo $defaultdata;

    $cookieS = base64_decode("HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=");

    echo "\n";
    echo $cookieS;

    echo "\n";
    echo($defaultdata ^ $cookieS);
?>