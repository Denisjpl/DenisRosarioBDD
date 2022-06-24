<?php
	session_start();
	$msg = $_GET['msg']
?>

<?php include('../templates/header.html'); ?>

<body>
    <h1>Pagina de login 33344</h1>
	<h3> Ingrese nombre de usuario y contraseña </h3>
	<br>
    <form class="form-signin" role="form" action="login_validation.php" method="post">
        <?php echo $msg; ?>
        <input type="text" name="username" placeholder="nombre de usuario" required autofocus>
        <input type="password" name="password" placeholder="contraseña" required>
        <button type="submit" name="login"> Iniciar sesión </button>
    </form>
    <form align="center" action="admin.php" method="get">
            <input type="submit" value="ADMIN">
    </form>

</body>