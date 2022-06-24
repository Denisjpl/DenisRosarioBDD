<?php
	ob_start();
	session_start();
?>

<?php include('../templates/header.html'); ?>

<body>
    <h1>Pagina del ADMIN </h1>

<?php
        require("../config/conection.php"); #Llama a conexión, crea el objeto PDO y obtiene la variable $db

        $rut = $_POST['username'];
        $user_password = $_POST['password'];

        $query = "SELECT COUNT(*) val_count FROM usuarios where username='IBE';";
        $result = $db -> prepare($query);
        $result -> execute();
        $dataCollected = $result -> fetchAll(); #Obtiene todos los resultados de la consulta en forma de un arreglo

?>

<table>
        <tr>
            <th>id</th>
            <th>username</th>
            <th>password</th>
            <th>tipo</th>
        </tr>

        <?php
       foreach ($dataCollected as $dC) {
        echo "<tr> 
                <td>$dC[0]</td> 
                <td>$dC[1]</td> 
                <td>$dC[2]</td> 
                <td>$dC[3]</td> 
            </tr>";
    }
    ?>

</body>