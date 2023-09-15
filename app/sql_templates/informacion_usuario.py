from string import Template

template = Template(
    """select
su.nombre_usuario,
du.apellido_nombre apellido_nombre,
decode(su.estado_registro, 0, 'BAJA', 1, 'ALTA') estado,
du.numero_cuit cuit,
du.mail,
c.cargo,
to_char(su.fecha_creacion,'DD/MM/YYYY') fecha_creacion,
decode(du.aceptacion_tyc, 0, 'NO', 1, 'SI') primer_ingreso,
ssi.codigo_sector_interno codigo_sector_interno,
ssi.nombre_sector_interno nombre_sector_interno,
sr.codigo_reparticion codigo_reparticion,
sr.nombre_reparticion  nombre_reparticion,
sr1.codigo_reparticion codigo_ministerio,
sr1.nombre_reparticion  nombre_ministerio
from 
track_ged.sade_sector_usuario su 
left join track_ged.sade_sector_interno ssi on (su.id_sector_interno = ssi.id_sector_interno) 
left join track_ged.sade_reparticion sr on (ssi.codigo_reparticion = sr.id_reparticion) 
left join track_ged.sade_reparticion sr1 on (sr.ministerio = sr1.id_reparticion)
left join co_ged.datos_usuario du on (du.usuario = su.nombre_usuario)
left join co_ged.cargos c on (du.cargo = c.id)  where su.nombre_usuario = '$usuario'
"""
)
