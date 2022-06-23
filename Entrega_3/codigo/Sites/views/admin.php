<?php
	session_start();
	$msg = $_GET['msg']
?>

<?php include('../templates/header.html'); ?>

<body>
    <h1>Pagina del ADMIN </h1>
	<?php
    require("../config/conection.php"); #Llama a conexión, crea el objeto PDO y obtiene la variable $db

    $query = "SELECT * FROM vuelos WHERE estado='pendiente';"; 
    $result = $db -> prepare($query);
    $result -> execute();
    $dataCollected = $result -> fetchAll(); #Obtiene todos los resultados de la consulta en forma de un arreglo
    ?>

    <table>
        <tr>
            <th>Vuelo id</th>
            <th>Aerodromo salida id</th>
            <th>Aerodromo llegada id</th>
            <th>Ruta id</th>
            <th>Codigo vuelo</th>
            <th>Codigo aereonave</th>
            <th>Codigo compañia</th>
            <th>Fecha salida</th>
            <th>Fecha llegada</th>
            <th>Velocidad</th>
            <th>Altitud</th>
            <th>Estado</th>
            <th>Valor</th>
            <th>Boton</th>
        </tr>
    <?php
        foreach ($dataCollected as $dC) {
        echo "<tr> 
                <td>$dC[0]</td> 
                <td>$dC[1]</td> 
                <td>$dC[2]</td> 
                <td>$dC[3]</td> 
                <td>$dC[4]</td> 
                <td>$dC[5]</td> 
                <td>$dC[6]</td> 
                <td>$dC[7]</td> 
                <td>$dC[8]</td> 
                <td>$dC[9]</td> 
                <td>$dC[10]</td> 
                <td>$dC[11]</td> 
                <td>$dC[12]</td> 
                <td><FORM ACTION='modificar_estado.php' METHOD='POST'><input type='submit' name=$dC[0] value='Aceptar/rechazar'/></FORM></td>
            </tr>";
    }
    ?>
    </table>

</body>