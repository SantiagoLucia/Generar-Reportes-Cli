from string import Template

template = Template(
    """select
ee.tipo_documento||'-'||ee.anio||'-'||ee.numero||'- -'||ee.codigo_reparticion_actuacion||'-'||ee.codigo_reparticion_usuario as nro_expediente, 
ee.codigo_reparticion_usuario as cod_reparticion_caratulacion, 
rep_caratula.nombre_reparticion as reparticion_caratulacion, 
min_caratula.codigo_reparticion as cod_organismo_caratulacion, 
min_caratula.nombre_reparticion as organismo_caratulacion, 
to_char(ee.fecha_creacion, 'DD/MM/YYYY') as fecha_caratulacion, 
to_char(ee.fecha_creacion, 'HH24:MI:SS') as hora_caratulacion,
tratas.codigo_trata,
tratas.descripcion as trata,  
ee.descripcion as descripcion, 
solex.motivo, 
ee.estado as estado_expediente,
nvl(regexp_substr(t.assignee_, '[^.]+', 1, 2),'simple') as tipo_tramitacion,
regexp_substr(t.assignee_, '[^.]+', 1, 1) as usuario_asignado,
du.apellido_nombre as nombre_apellido,
coalesce(regexp_substr(regexp_substr(p.groupid_, '[^-]+', 1, 2),'[^.]+', 1, 1),ssi.codigo_sector_interno) as sector_actual,
repfin.codigo_reparticion as cod_reparticion_actual,
repfin.nombre_reparticion as reparticion_actual,
minfin.codigo_reparticion as cod_organismo_actual,  
minfin.nombre_reparticion as organismo_actual,
ee.usuario_modificacion,
to_char(ee.fecha_modificacion, 'DD/MM/YYYY') as fecha_ultima_modificacion, 
to_char(ee.fecha_modificacion, 'HH24:MI:SS') as hora_ultima_modificacion,
round(sysdate - ee.fecha_creacion) as dias_abierto
from
ee_ged.ee_expediente_electronico ee
left join ee_ged.solicitud_expediente solex on solex.id = ee.solicitud_iniciadora
left join ee_ged.trata tratas on tratas.id = ee.id_trata
left join ee_ged.jbpm4_task t on t.execution_id_ = ee.id_workflow
left join ee_ged.jbpm4_participation p on p.task_ = t.dbid_
--Caratulacion--
left join track_ged.sade_reparticion rep_caratula on ee.codigo_reparticion_usuario = rep_caratula.codigo_reparticion
left join track_ged.sade_reparticion min_caratula on rep_caratula.ministerio = min_caratula.id_reparticion
--Esta asignado a usuario--
left join track_ged.sade_sector_usuario su on regexp_substr(t.assignee_, '[^.]+', 1, 1) = su.nombre_usuario
and su.id_sector_usuario = (
    select max(z.id_sector_usuario) from track_ged.sade_sector_usuario z 
    where z.nombre_usuario = regexp_substr(t.assignee_, '[^.]+', 1, 1)
    )
left join co_ged.datos_usuario du on du.usuario = su.nombre_usuario
left join track_ged.sade_sector_interno ssi on su.id_sector_interno = ssi.id_sector_interno
left join track_ged.sade_reparticion sr on ssi.codigo_reparticion = sr.id_reparticion
left join track_ged.sade_reparticion sr1 on sr1.id_reparticion = sr.ministerio
--Sin asignar a usuario--
left join track_ged.sade_reparticion repa on regexp_substr(p.groupid_, '[^-]+', 1, 1) = repa.codigo_reparticion
left join track_ged.sade_reparticion ministerio on ministerio.id_reparticion = repa.ministerio
--Reparticion/Ministerio actual
left join track_ged.sade_reparticion repfin on repfin.codigo_reparticion = coalesce(sr.codigo_reparticion, repa.codigo_reparticion)
left join track_ged.sade_reparticion minfin on minfin.codigo_reparticion = coalesce(sr1.codigo_reparticion, ministerio.codigo_reparticion)
where
ee.codigo_reparticion_usuario in ($reparticiones)
and ee.fecha_creacion between to_date('$fecha_inicio','DD/MM/YYYY') and to_date('$fecha_fin','DD/MM/YYYY')+1
"""
)
