import argparse

parser = argparse.ArgumentParser(
    prog="APP",
    description="Generar reportes",
)
parser.add_argument(
    "--consulta",
    action="store",
    help="Nombre de la consulta (Ej: expedientes_caratulados)",
    required=True,
)
parser.add_argument(
    "--organismo",
    action="store",
    help="Codigo de organismo (Ej: TESTGDEBA)",
    required=True,
)
parser.add_argument(
    "--parametros",
    action="store",
    help="Valores de los parametros para la consulta (Ej: '01/01/2023 01/09/2023 TEST0001')",
    required=True,
)

options = parser.parse_args()
