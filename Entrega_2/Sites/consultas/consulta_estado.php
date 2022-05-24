<?php include('../templates/header.html');   ?>

<body>

  <?php
  require("../config/conexion.php"); #Llama a conexión, crea el objeto PDO y obtiene la variable $db

  $var = $_POST["estado"];
  $query = "SELECT * FROM vuelos WHERE estado='$var';";
  $result = $db -> prepare($query);
  $result -> execute();
  $dataCollected = $result -> fetchAll(); #Obtiene todos los resultados de la consulta en forma de un arreglo
  ?>

  <table>
    <tr>
      <th>Vuelo id</th>
      <th>Aerodromo llegada id</th>
      <th>Aerodromo salida id</th>
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
    </tr>
  <?php
  foreach ($dataCollected as $dC) {
    echo "<tr> <td>$dC[0]</td> <td>$dC[1]</td> <td>$dC[2]</td> <td>$dC[3]</td> <td>$dC[4]</td> <td>$dC[5]</td> <td>$dC[6]</td> <td>$dC[7]</td> <td>$dC[8]</td> <td>$dC[9]</td> <td>$dC[10]</td> <td>$dC[11]</td> <td>$dC[12]</td>  </tr>";
  }
  ?>
  </table>

<?php include('../templates/footer.html'); ?>
