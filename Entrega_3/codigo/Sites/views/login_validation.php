<?php
	session_start();
	$msg = $_GET['msg']
?>

<?php include('../templates/header.html'); ?>

<body>
    <h1>Pagina del login validation </h1>
	<?php
    require("../config/conection.php"); #Llama a conexión, crea el objeto PDO y obtiene la variable $db
    $username = $_POST['username'];
    $user_password = $_POST['password'];

    $query = "SELECT COUNT(*) val_count FROM usuarios where username='IBE';";
    $result = $db -> prepare($query);
    $result -> execute();
    $dataCollected = $result -> fetchAll(); #Obtiene todos los resultados de la consulta en forma de un arreglo
    ?>

    <table>
        <tr>
            <th>Vuelo id</th>
        </tr>
    <?php
        foreach ($dataCollected as $dC) {
        echo "<tr> 
                <td>$dC[0]</td> 
            </tr>";
    }
    print("Este es el numero de confirmacion: $confirmacion");
    ?>
    </table>

</body>
