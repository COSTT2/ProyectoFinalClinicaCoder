# Proyecto Final Academia Coder

Este proyecto intenta crear un sistema funcional para la administracion y uso de una plataforma tipo academia.
Cosas que se pueden hacer actualmente:
- Crear, leer, editar y borrar Cursos.
- Crear, leer, editar y borrar Articulos los cuales son enviados por el administrador hacia una pagina principal que puede ser vista por los usuarios de la academia.
- Crear, leer, editar y borrar Profesores.
- Crear, leer y editar Usuarios.
- Posibilidad de login y registro como estudiante.
- Posibilidad de entrar al campus siendo estudiante y contar con ciertas caracteristicas del campus.
- Posibilidad de entrar al campus como administrador para hacer un manejo de datos de manera eficiente. 

# Instalación

Para instalar este software se necesita:

## Check version de python
Este proyecto esta escrito con python 3.9.12. Se sugiere probar con esta version o con una version superior para no tener problemas de compatibilidad.

Como chequear la version de python 

para *nix systems:

```bash
> python --version
> Python 3.8.0
```

para windows:

```bash
c:\> py --version
c:\> Python 3.8.0
```

## Instalar Dependencias

Para instalar las dependencias se necesita correr `pip install`, asegurarse de que se encuentran en la carpeta del proyecto antes de realizar cualquier comando.

```bash
> pip install -r requirements.txt
```

`Algunos sistemas operativos necesitaran de pip3 en vez de pip `

## Configurando Django

Luego de instalar las dependencias hace falta correr un par de comandos de Django

### Migraciones

*nix:
```bash
> python mananage.py migrate
```
windows:
```bash
c:\> py mananage.py migrate
```

### Correr la prueba de servidor

```bash
> python mananage.py runserver
```
windows:
```bash
c:\> py mananage.py runserver
```
Dirigirse a localhost:8000/

para acceder a la aplicación.

Si todo va bien deberías poder ver la pagina de inicio y la aplicación funcionando.
