<?php

    function teacher(){
        echo "I am a teacher";
    }

    function student($name){
        echo "I am a student and my name is $name";
    }

    $fun_teacher = "teacher";
    $fun_student = "student";

    $fun_teacher();
    echo "\n";
    $fun_student("Joe");

?>