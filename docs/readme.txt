Instalación:
-----------
pip install -r requirements.txt

Ejecución:
---------
main.py --organismo <"codigo_organismo"> --consulta <"nombre_consulta"> --parametros <"param1,param2,...,paramn">

La salida de guarda en /app/salida en formato JSON

Test:
-----
main.py --organismo test --consulta test --parametros test
salida de consola: Archivo test_test.json generado - 1 registros.
test_test.json -> [{"dummy":"X"}]