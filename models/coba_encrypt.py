# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class coba_encrypt(models.Model):
    _name = "coba.encrypt"
    _description = 'Uji coba field_encryption'

    name = fields.Char("Name")
    sandi = fields.Encrypted()
    kata_sandi = fields.Char('Kata Sandi', encrypt='sandi')
    angka_sandi = fields.Integer('Angka Sandi', encrypt='sandi')

