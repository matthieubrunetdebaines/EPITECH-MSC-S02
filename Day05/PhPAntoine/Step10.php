<?php

    function print_calls(){
        static $callCount = 0;
        $callCount++;
        echo $callCount  ."\n";
    }

    print_calls();
    print_calls();
    print_calls();

?>