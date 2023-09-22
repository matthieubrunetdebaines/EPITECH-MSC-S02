<?php

    function calc(string $operation, int $nb1, int $nb2){
        
        $result = eval("return $nb1 $operation $nb2;");
        return $result;

    }

    print_r(calc("+", 2, 1));




?>