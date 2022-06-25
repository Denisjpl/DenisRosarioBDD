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


    $query = "SELECT COUNT(*) val_count FROM usuarios where (username='$username') AND (contrasena='$user_password');";
    $result = $db -> prepare($query);
    $result -> execute();
    $dataCollected = $result -> fetchAll(); #Obtiene todos los resultados de la consulta en forma de un arreglo
    if($dataCollected[0][0] > 0){
        $query = "SELECT * FROM usuarios where (username='$username') AND (contrasena='$user_password');";
        $result = $db -> prepare($query);
        $result -> execute();
        $dataCollected = $result -> fetchAll(); #Obtiene todos los resultados de la consulta en forma de un arreglo
        print_r($dataCollected[0][3]);
        if ($dataCollected[0][3] == 'admin'){
            print_r($dataCollected[0][1]);
            $_SESSION['valid'] = true;
            $_SESSION['timeout'] = time();
            $_SESSION['username'] = $_POST['username'];
            $_SESSION['password'] = $_POST['password'];
            $msg = "Sesión iniciada por admin";
            header("Location: ../index.php?msg=$msg");
        } else if ($dataCollected[0][3] == 'compania'){
            print_r($dataCollected[0][1]);
            $_SESSION['valid'] = true;
            $_SESSION['timeout'] = time();
            $_SESSION['username'] = $_POST['username'];
            $_SESSION['password'] = $_POST['password'];
            $msg = "Sesión iniciada por compania";
            header("Location: ../index.php?msg=$msg");
        }else{
            print_r($dataCollected[0][1]);
            $_SESSION['valid'] = true;
            $_SESSION['timeout'] = time();
            $_SESSION['username'] = $_POST['username'];
            $_SESSION['password'] = $_POST['password'];
            $msg = "Sesión iniciada por usuario";
            header("Location: ../index.php?msg=$msg");
        }


    }else{
        $query = "SELECT * FROM usuarios where (username='$username') AND (contrasena='$user_password');";
        $result = $db -> prepare($query);
        $result -> execute();
        $dataCollected = $result -> fetchAll(); #Obtiene todos los resultados de la consulta en forma de un arreglo
        print_r('0');
    }
    ?>

</body>

