<?php
    $defaultdata = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));

    echo $defaultdata."\nn";
    
    $key = "eDWo";

    
    $out = "";
    for($i=0; $i < strlen($defaultdata); $i++){
    	$out .= $defaultdata[$i] ^ $key[$i % strlen($key)];
    }
    
    echo base64_encode($out);
?>