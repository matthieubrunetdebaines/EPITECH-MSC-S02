<?php

    function get_args(){

        $args = func_get_args();
        return $args;

    }

    function get_last_arg(){

        $args = func_get_args();
        $last_arg= $args[count($args)-1];
        return $last_arg;

    }

    print_r(get_args("pomme", "peche", "poire", "abricot"));
    print_r(get_last_arg("pomme", "peche", "poire", "abricot"));

?>