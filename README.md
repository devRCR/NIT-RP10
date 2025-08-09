<p align="center">
  <img src="images/img_01.png" alt="Neutron Imaging Facility" width="400"/>
</p>

# NIT-RP10: Neutron Imaging and Tomography Facility of the RP10 Research Reactor

Este repositorio contiene el código y documentación relacionados con la instalación y operación de la instalación de Imagenología y Tomografía por Neutrones del reactor de investigación RP10.

## Descripción

NIT-RP10 es una plataforma para la obtención de imágenes y tomografías utilizando neutrones, permitiendo el análisis no destructivo de materiales y componentes.

## Estructura del repositorio

- `images/`: Imágenes y diagramas del proyecto.
- `src/`: Código fuente principal.
- `docs/`: Documentación técnica y manuales de usuario.

## Requisitos

Asegúrate de tener instaladas las siguientes dependencias en tu entorno Python:

| Paquete             | Versión   |
|---------------------|-----------|
| asi                 | 0.1.0     |
| numpy               | 2.2.6     |
| pillow              | 11.3.0    |
| pip                 | 22.0.2    |
| PyQt5               | 5.15.11   |
| PyQt5-Qt5           | 5.15.17   |
| PyQt5_sip           | 12.17.0   |
| pyserial            | 3.5       |
| PySide6             | 6.9.1     |
| PySide6_Addons      | 6.9.1     |
| PySide6_Essentials  | 6.9.1     |
| setuptools          | 59.6.0    |
| shiboken6           | 6.9.1     |

## Instalación rápida de dependencias

Puedes instalar la mayoría de las dependencias (excepto `asi`) con el siguiente comando:

```bash
pip install numpy==2.2.6 pillow==11.3.0 pyserial==3.5 PyQt5==5.15.11 PySide6==6.9.1 PySide6-Addons==6.9.1 PySide6-Essentials==6.9.1 shiboken6==6.9.1 setuptools==59.6.0
```

**Nota:**  
La biblioteca `asi` debe instalarse manualmente desde el repositorio oficial:

```bash
git clone https://github.com/seeing-things/zwo.git
cd zwo-master/python
pip install . --use-pep517
```

## Uso

1. Clona este repositorio:
   ```bash
   git clone https://github.com/devRCR/NIT-RP10.git
   ```
2. Instala las dependencias necesarias (ver arriba).
3. Sigue las instrucciones en la documentación para comenzar a utilizar la plataforma.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerencias o mejoras.

## Licencia

Este proyecto está bajo la licencia MIT.
