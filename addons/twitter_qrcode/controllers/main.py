from odoo import http
from odoo.http import request
import base64

class TwitterQRController(http.Controller):

    @http.route('/twitter-qr', type='http', auth='public', website=True)
    def twitter_qr_page(self, **kwargs):
        accounts = request.env['twitter.account'].sudo().search([('active', '=', True)])
        return request.render('twitter_qrcode.twitter_qr_template', {
            'accounts': accounts
        })

    @http.route('/twitter-qr/download/<int:account_id>', type='http', auth='public')
    def download_qr(self, account_id, **kwargs):
        """Download the QR code as PNG attachment"""
        account = request.env['twitter.account'].sudo().browse(account_id)
        if not account or not account.qr_code:
            return request.not_found()
        
        qr_bytes = base64.b64decode(account.qr_code)
        filename = f"{account.name.replace(' ', '_')}_qr.png"

        return request.make_response(
            qr_bytes,
            headers=[
                ('Content-Type', 'image/png'),
                ('Content-Disposition', f'attachment; filename="{filename}"')
            ]
        )