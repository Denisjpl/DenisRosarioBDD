<?php
	session_start();
	$msg = $_GET['msg']
?>

<?php

    require("../config/conection.php"); #Llama a conexión, crea el objeto PDO y obtiene la variable $db

    $id_vuelo = $_POST["id_vuelo"];

    $query = "UPDATE vuelos SET estado='rechazado' WHERE vuelo_id=$id_vuelo;";
    $result = $db -> prepare($query);
    $result -> execute();
    $msg = "Valor Aceptado";
    header("Location: admin.php?msg=$msg");
?>