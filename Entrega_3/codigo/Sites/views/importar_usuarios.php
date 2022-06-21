<?php
	ob_start();
	session_start();
?>

<?php

    require("../config/conection.php"); #Llama a conexión, crea el objeto PDO y obtiene la variable $db

    $query = "SELECT mover_usuario();";
    $result = $db -> prepare($query);
    $result -> execute();
    $msg = "Datos Importados correctamente";
    header("Location: ../index.php?msg=$msg");
?>