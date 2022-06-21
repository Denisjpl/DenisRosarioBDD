<?php include('templates/header.html');   ?>

<body>
  <h1 align="center">Vuelos Aereos</h1>
  <p style="text-align:center;">En esta pagina encontraras toda la informacion de sobre tus vuelos aereos :).</p>

  <!-- Consulta numero 1, se agrega una opcion para ver todos los estados, pero la consulta se contesta poniendo
  la opcion de 'pendiente' -->
  <p style="text-align:center;">Consulta 1.</p>
  <!-- Primero ponemos visualmente la opciones que puede elegir el usuario -->
  <?php
  #Primero obtenemos todos los tipos de estados de los vuelos
  require("config/conexion.php");
  $result = $db -> prepare("SELECT DISTINCT estado FROM vuelos;");
  $result -> execute();
  $dataCollected = $result -> fetchAll();
  ?>

<!-- Creamos el form para hacer la consulta numero 1 -->
<form align="center" action="consultas/consulta_estado.php" method="post">
    Seleccinar un estado del vuelos: 
    <select name="estado">
      <?php
      #Para cada estado agregamos el tag <option value=value_of_param> visible_value </option>
      foreach ($dataCollected as $d) {
        echo "<option value=$d[0]>$d[0]</option>";
      }
      ?>
    </select>
    <br><br>
    <input type="submit" value="Buscar por estado">
  </form>

  <br>
  <br>
  
  <!-- Creamos un form con una cuadricula para que le usuario elija sus opciones -->
  <p style="text-align:center;">Consulta 2.</p>

  <h3 align="center"> ¿Que tipo de vuelo quieres ver?</h3>
  
  <form align="center" action="consultas/consulta_codigo-ICAO_aerolinea.php" method="post">
    Código_ICAO:
    <input type="text" name="codigo_ICAO_elegido">
    <br/>
    Aerolínea:
    <input type="text" name="nombre_aerolinea">
    <br/><br/>
    <input type="submit" value="Buscar">
  </form>
  
  <br>
  <br>
  <br>

  <p style="text-align:center;">Consulta 3.</p>

  <h3 align="center"> ¿Quieres ver los ticket de un cliente? </h3>

  <form align="center" action="consultas/consulta_codigo_reserva.php" method="post">
    Código de reserva:
    <input type="text" name="codigo_reserva_elegido">
    <br/><br/>
    <input type="submit" value="Buscar">
  </form>
  
  <br>
  <br>
  <br>

  <p style="text-align:center;">Consulta 4.</p>
  <h3 align="center"> Aqui estaria nuestra consulta 4, solo si la tuvieramos :(</h3>

</body>
</html>
