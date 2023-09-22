<?php

    function spupof(string $str){

        $result="";
        for ($i=0; $i<strlen($str); $i++ ){

            $caractere = $str[$i];
            if (ctype_alpha($caractere)){

                $caractere = strtolower($caractere);
                $caractere = chr(((ord($caractere)-ord("a")+1)%26)+ord("a"));

                $result.=$caractere."\n";
            }

        }
        
        return $result;
    }

print_r(spupof("CoUcOu lEs gEnS"));

?>