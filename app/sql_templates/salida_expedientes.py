from string import Template

template = Template(
    """select 
'EX-'||regexp_substr(h.expediente,'[0-9]{4}',1)||'-'|| 
    regexp_substr(h.expediente,'[0-9]+',7)||'- -GDEBA-'||
    regexp_substr(h.expediente,'[^-]+',1,2) as numero_expediente,
h.tipo_operacion as operacion,
to_char(h.fecha_operacion,'DD/MM/YYYY') as fecha_operacion,
h.usuario as usuario_operacion,
h.sector_usuario_origen as sector_operacion,
h.reparticion_usuario as reparticion_operacion,
h.codigo_jurisdiccion_origen as jurisdiccion_operacion,
h.motivo,
h.estado,
h.destinatario,
h.codigo_sector_destino,
h.codigo_reparticion_destino,
h.codigo_jurisdiccion_destino

from ee_ged.historialoperacion h
where h.fecha_operacion > to_date('$fecha_inicio','DD/MM/YYYY')
and h.tipo_operacion = 'Pase'
and h.codigo_jurisdiccion_origen = '$codigo_organismo'
and h.codigo_jurisdiccion_destino != '$codigo_organismo'
order by h.id desc
"""
)
