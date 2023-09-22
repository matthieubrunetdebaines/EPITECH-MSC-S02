<?php

    $nb_a =10;
    $nb_b = 5;

    function my_sub(){
        // utilisation des var globales
        global $nb_a, $nb_b; 

        $resultat = $nb_a - $nb_b;
        $nb_a = $resultat;

        return $nb_a;
    }

    print_r(my_sub());

?>