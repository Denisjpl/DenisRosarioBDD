<?php include('../templates/header.html');   ?>

<body>
<?php
  #Llama a conexión, crea el objeto PDO y obtiene la variable $db
  require("../config/conexion.php");

  $codigo_reserva = $_POST["codigo_reserva_elegido"];

 	$query = "SELECT TRCP.pasaporte, TRCP.nombre, TRCP.nacionalidad, TRCP.fecha_nacimiento, TRCP.codigo_reservas, TRCP.numero_ticket, TRCP.numero_asiento, TRCP.clase, TRCP.comida_y_maleta, V.valor FROM vuelos V, (SELECT CP.pasaporte, CP.nombre, CP.nacionalidad, CP.fecha_nacimiento, TR.codigo_reservas, TR.numero_ticket, TR.numero_asiento, TR.clase, TR.comida_y_maleta, TR.vuelo_id FROM cliente_pasajero CP, (SELECT T.codigo_reservas, T.numero_ticket, T.numero_asiento, T.clase,T.comida_y_maleta, R.pasaporte_pasajero, R.vuelo_id FROM ticket T, reserva R WHERE (T.codigo_reservas = '$codigo_reserva') AND (T.numero_ticket = R.numero_ticket)) as TR WHERE TR.pasaporte_pasajero = CP.pasaporte) as TRCP WHERE TRCP.vuelo_id = V.vuelo_id;";
	$result = $db -> prepare($query);
	$result -> execute();
	$DataCollected = $result -> fetchAll();
  ?>

	<table>
    <tr>
      <th>Pasaporte</th>
      <th>Nombre</th>
      <th>Nacionalidad</th>
      <th>Fecha Nacimiento</th>
      <th>Codigo Reserva</th>
      <th>Numero ticket</th>
      <th>Numero asiento</th>
      <th>Clase</th>
      <th>Comida y maleta</th>
      <th>Costo</th>
    </tr>
  <?php
	foreach ($DataCollected as $dC) {
  		echo "<tr><td>$dC[0]</td><td>$dC[1]</td><td>$dC[2]</td><td>$dC[3]</td><td>$dC[4]</td><td>$dC[5]</td> <td>$dC[6]</td> <td>$dC[7]</td> <td>$dC[8]</td> <td>$dC[9]</td></tr>";
	}
  ?>
	</table>

<?php include('../templates/footer.html'); ?>
