<?php

    function swap_variables($a,$b){
        $c=$b;
        $b=$a;
        $a=$c;

        return "variable a: ".$a. "\nvariable b: ". $b;
    }

    print_r(swap_variables(50, 10));

?>