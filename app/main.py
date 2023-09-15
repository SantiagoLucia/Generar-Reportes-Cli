import database
import os
from sql_templates import test, informacion_usuario, expedientes_caratulados
from options import options
from pathlib import Path

templates = {
    "test": test.template,
    "informacion_usuario": informacion_usuario.template,
    "expedientes_caratulados": expedientes_caratulados.template,
}


def main() -> None:
    consulta = options.consulta
    organismo = options.organismo
    parametros = (options.parametros).split(",")

    template = templates.get(consulta)
    if not template:
        print("ERROR - No existe la consulta solicitada.")
        return

    identificadores = template.get_identifiers()
    try:
        mapeo = {
            identificador: parametros[i]
            for i, identificador in enumerate(identificadores)
        }
    except:
        print(f"ERROR - Numero incorrecto de parametros.\n{identificadores}")
        return

    sql = template.substitute(**mapeo)

    nro_registros = 0
    path_archivo = (
        f"{Path(__file__).resolve().parent}/salida/{organismo}/{consulta}.json"
    )

    if os.path.exists(path_archivo):
        os.remove(path_archivo)

    with open(path_archivo, "a", encoding="utf-8") as file:
        for data in database.ejecutar_consulta(sql):
            data.to_json(
                file,
                orient="records",
                force_ascii=False,
            )
            nro_registros += len(data.index)

    print(
        f"Carpeta {organismo} y archivo {consulta}.json generado - {nro_registros} registros."
    )


if __name__ == "__main__":
    main()
