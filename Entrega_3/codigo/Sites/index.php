<?php session_start();
    if (isset($_SESSION['username'])){
        echo "Bienvenido/a: ";
        echo $_SESSION['username'];
    }
?>

<?php
    include("templates/header.html");
?>

<body>
    <h1> Entrega 3</h1>
    <br>
    <?php
        if (!isset($_SESSION['username'])) {
    ?>
        <h2>Estoy en el if</h2>
        <form align="center" action="views/importar_usuarios.php" method="get">
            <input type="submit" value="Importar Usuarios">
        </form>
        <form align="center" action="views/login.php" method="get">
            <input type="submit" value="Iniciar sesión">
        </form>
        <?php } else { ?>
            <h2>Estoy en el else</h2>
            <form align="center" class="form-signin" role="form" action="login_validation.php" method="post">
            <input type="text" name="username" placeholder="nombre de usuario" required autofocus>
            <input type="password" name="password" placeholder="contraseña" required>
        <button type="submit" name="login"> Iniciar sesión </button>
        </form>
        <form align="center" action="logout.php" method="post">
            <input type="submit" value="Cerrar sesión">
        </form>
    <?php } ?>
</body>

</html>