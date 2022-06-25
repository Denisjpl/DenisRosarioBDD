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

    $query = "SELECT COUNT(*) val_count FROM usuarios where (username=$username) AND (contrasena=$user_password);";
    $result = $db -> prepare($query);
    $result -> execute();
    $dataCollected_1 = $result -> fetchAll(); #Obtiene todos los resultados de la consulta en forma de un arreglo
    print_r($dataCollected_1[0]);
    if($dataCollected[0][0] > 0){
        $query = "SELECT * FROM usuarios where (username=$username) AND (contrasena=$user_password);";
        $result = $db -> prepare($query);
        $result -> execute();
        $dataCollected_2 = $result -> fetchAll(); #Obtiene todos los resultados de la consulta en forma de un arreglo

        if ($dataCollected_2[0][3] == 'admin'){
            // $_SESSION['valid'] = true;
            // $_SESSION['timeout'] = time();
            // $_SESSION['username'] = $_POST['username'];
            // $_SESSION['password'] = $_POST['password'];
            // $msg = "Sesión iniciada por admin";
            // header("Location: ../index.php?msg=$msg");
        }
    } else{
        $msg = "Sesión iniciada correctamente";
        // header("Location: admin.php?msg=$msg");
    }
        ?>
</body>

