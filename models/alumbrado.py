# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
import psycopg2
from odoo.addons.base_geoengine.fields import GeoPoint
from osgeo import ogr

class solicitud(models.Model):
    _name = 'alumbrado.view.read.online'
    _auto = False

    xap_comp = fields.Char()
    xap = fields.Float()
    cvecol = fields.Float()
    colonia = fields.Char()
    cvecalle = fields.Float()
    calle = fields.Char()
    tipo_c = fields.Char()
    entre = fields.Char()
    t_piso = fields.Char()
    nivel_c = fields.Char()
    ancho_c = fields.Char()
    mod_lam = fields.Char()
    tecno = fields.Char()
    capac_pot = fields.Float()
    marca_foco = fields.Char()
    marca_bala = fields.Char()
    perdidas = fields.Float()
    tension = fields.Char()
    tipodeilum = fields.Char()
    zona_cfe = fields.Char()
    tipoposte = fields.Char()
    no_lum = fields.Float()
    altura_p = fields.Float()
    altura_lum = fields.Char()
    brazo = fields.Char()
    jefe_cua = fields.Char()
    unidad = fields.Float()
    fecha_cens = fields.Date()
    imagen = fields.Char()
    x = fields.Float()
    y = fields.Float()
    observ = fields.Char()
    servicio = fields.Char()
    rpu = fields.Char()
    medidor = fields.Char()
    #geom geometry = fiels.Point()

    @api.model_cr# cr=cursor  //Instancia de una Clase en Odoo
    def init(self):
        tools.drop_view_if_exists(self._cr, 'alumbrado_view_read_online')# toolsviewifexists=Informes modelos mediante vistas de PostgreSQL
        consulta = "CREATE OR REPLACE VIEW public.alumbrado_view_read_online AS(select gid as id, xap_comp as xap_comp, xap as xap, cvecol as cvecol, colonia as colonia, cvecalle as cvecalle, calle as calle, tipo_c as tipo_c, entre as entre, t_piso as t_piso, nivel_c as nivel_c, ancho_c as ancho_c, mod_lam as mod_lam, tecno as tecno, capac_pot as capac_pot, marca_foco as marca_foco, marca_bala as marca_bala, perdidas as perdidas, tension as tension, tipodeilum as tipodeilum, zona_cfe as zona_cfe, tipoposte as tipoposte, no_lum as no_lum, altura_p as altura_p, altura_lum as altura_lum, brazo as brazo, jefe_cua as jefe_cua, unidad as unidad, fecha_cens as fecha_cens, imagen as imagen, x as x, y as y, observ as observ, servicio as servicio, rpu as rpu, medidor as medidor from alumbrado)"
        self._cr.execute(consulta)







