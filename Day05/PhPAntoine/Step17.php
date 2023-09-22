<?php

    function array_key(array $array, int $key){
        return $array[$key];
    }

    print_r(array_key([1, 2, 3, 4], 2));
?>