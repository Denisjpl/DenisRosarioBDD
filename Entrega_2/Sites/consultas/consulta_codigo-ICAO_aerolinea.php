<?php include('../templates/header.html');   ?>

<body>

<?php
  #Llama a conexión, crea el objeto PDO y obtiene la variable $db
  require("../config/conexion.php");

	$codigo_ICAO = $_POST["codigo_ICAO_elegido"];
	$aerolinea = $_POST["nombre_aerolinea"];

 	$query = "SELECT vuelo_id, aerodromo_salida_id, aerodromo_llegada_id, ruta_id, codigo_vuelo, codigo_aeronave, vuelos.codigo_compania, fecha_salida, fecha_llegada, velocidad, altitud, estado, valor FROM vuelos, (SELECT aerodromo.aerodromo_id, compania.codigo_compania FROM aerodromo, compania WHERE (aerodromo.codigo_ICAO = '$codigo_ICAO') AND (compania.nombre_compania = '$aerolinea')) as A WHERE (A.aerodromo_id = vuelos.aerodromo_llegada_id) AND (A.codigo_compania = vuelos.codigo_compania);";
	$result = $db -> prepare($query);
	$result -> execute();
	$dataCollected = $result -> fetchAll();
	
?>


	<table>
		<tr>
		<th>Vuelo ID</th>
		<th>Aerodromo salida id</th>
		<th>Aerodromo llegada id</th>
		<th>Ruta id</th>
		<th>Codigo vuelo</th>
		<th>Codigo aeronave</th>
		<th>Codigo compañia</th>
		<th>Fecha salida</th>
		<th>Fecha llegada</th>
		<th>Velocidad</th>
		<th>Altitud</th>
		<th>Estado</th>
		<th>Valor</th>
			
		</tr>
	<?php
	foreach ($dataCollected as $dC) {
		echo "<tr> <td>$dC[0]</td> <td>$dC[1]</td> <td>$dC[2]</td> <td>$dC[3]</td> <td>$dC[4]</td> <td>$dC[5]</td> <td>$dC[6]</td> <td>$dC[7]</td> <td>$dC[8]</td> <td>$dC[9]</td> <td>$dC[10]</td> <td>$dC[11]</td> <td>$dC[12]</td> </tr>";
		}
	?>
	</table>
	
<?php include('../templates/footer.html'); ?>