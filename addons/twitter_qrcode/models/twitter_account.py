from odoo import models, fields, api, _
import qrcode
import base64
from io import BytesIO

class TwitterAccount(models.Model):
    _name = 'twitter.account'
    _description = 'Twitter Account'

    name = fields.Char(string="Display Name", required=True)
    twitter_handle = fields.Char(string="Twitter Handle", required=True)
    twitter_url = fields.Char(string="Twitter URL", compute="_compute_url")
    qr_code = fields.Binary(string="QR Code")
    active = fields.Boolean(default=True)

    @api.depends('twitter_handle')
    def _compute_url(self):
        for record in self:
            if record.twitter_handle:
                handle = record.twitter_handle.replace("@", "")
                record.twitter_url = f"https://x.com/{handle}"
                record._generate_qr()
            else:
                record.twitter_url = False

    def _generate_qr(self):
        for record in self:
            if record.twitter_url:
                qr = qrcode.make(record.twitter_url)
                buffer = BytesIO()
                qr.save(buffer, format="PNG")
                record.qr_code = base64.b64encode(buffer.getvalue())

    def action_regenerate_qr(self):
        self._generate_qr()