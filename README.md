# Sistema Simple de Reportes Financieros (Python)

## Descripcion breve
Este proyecto implementa un sistema interno simple para generar y transformar reportes financieros automaticos.
Se aplican solo patrones de diseno estudiados y seleccionados para este caso:

- strategy
- decorator
- factory

No incluye interfaz grafica ni canales reales de infraestructura. La entrega se simula por consola para mantener el ejemplo simple.

## Patrones aplicados y justificacion

### 1) Strategy
Se usa para cambiar la logica de procesamiento segun el tipo de usuario:

- `ExecutiveStrategy`
- `AuditorStrategy`
- `AnalystStrategy`

Beneficio: permite agregar nuevos tipos de procesamiento sin modificar la logica principal.

### 2) Decorator
Se usa para agregar mejoras opcionales al contenido del reporte de forma combinable:

- `HeaderDecorator`
- `WatermarkDecorator`
- `EncryptionDecorator` 

Beneficio: evita crear muchas subclases y permite encadenar mejoras sin tocar la clase base.

### 3) Factory
Se usa para centralizar la creacion de objetos:

- `StrategyFactory` para estrategias por tipo de usuario.
- `FormatterFactory` para formato de salida (`pdf`, `excel`, `csv`).

Beneficio: reduce condicionales repetidos y desacopla la logica de instanciacion.

### 4) Delivery Factory
Se usa para elegir el canal de entrega del reporte sin cambiar la logica principal:

- `EmailDelivery`
- `SharedFolderDelivery`
- `ApiDelivery`

Beneficio: permite agregar nuevos canales de entrega sin modificar el flujo del reporte.



## Estructura
- `src/reporting/models.py`: modelo de datos del reporte.
- `src/reporting/strategies.py`: estrategia por tipo de usuario.
- `src/reporting/decorators.py`: decoradores del contenido.
- `src/reporting/formatters.py`: formateadores de salida.
- `src/reporting/factories.py`: fabricas de estrategias y formatos.
- `src/reporting/delivery.py`: canales de entrega y fabrica de entrega.
- `src/reporting/service.py`: servicio de generacion.
- `src/reporting/__init__.py`: facilita importar las clases principales desde un solo lugar.
- `main.py`: ejecucion de casos de verificacion.

## Casos de verificacion implementados
1. Ejecutivo + PDF + sin decoradores.
2. Auditor + Excel + HeaderDecorator.
3. Analista + CSV + HeaderDecorator + WatermarkDecorator.
4. Entrega simulada por correo, carpeta compartida y API.

## Ejecucion
```bash
python main.py
```

## Repositorio

`https://github.com/luishumbertonavarro/Modulo1-Arq-MServices`
