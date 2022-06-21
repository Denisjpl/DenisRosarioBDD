CREATE OR REPLACE FUNCTION

-- declaramos la función y sus argumentos
mover_usuario()

-- declaramos lo que retorna, en este caso un booleano
RETURNS void AS $$

-- declaramos las variables a utilizar
DECLARE

tupla_1 RECORD;
tupla_2 RECORD;

-- RECORD es un tipo (en realidad placeholder) que permite almacenar filas
-- más información sobre variables en https://www.postgresql.org/docs/9.1/plpgsql-declarations.html

-- definimos nuestra función
BEGIN

    INSERT INTO usuarios (username, contrasena, tipo) values('DGCA', 'admin', 'admin');

    FOR tupla_1 IN (SELECT codigo_compania FROM compania)

    LOOP
        INSERT INTO usuarios (username, contrasena, tipo) values(tupla_1.codigo_compania, round(random() * 100000000), 'compania');
    END LOOP;

    FOR tupla_2 IN (SELECT pasaporte FROM cliente_pasajero)

    LOOP
        INSERT INTO usuarios (username, contrasena, tipo) values(tupla_2.pasaporte, 'contrasena', 'usuario');
    END LOOP;


-- finalizamos la definición de la función y declaramos el lenguaje
END
$$ language plpgsql