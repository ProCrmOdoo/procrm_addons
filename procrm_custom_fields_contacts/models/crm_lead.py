from odoo import api, fields, models



class CrmLead(models.Model):
    _inherit = 'crm.lead'

    traffic_source = fields.Many2one(comodel_name='traffic.source', string="Traffic source")
    more_source = fields.Char(string="More source")
    deal_type = fields.Many2one(comodel_name='deal.type', string="Deal type")
    Facebook = fields.Char(string="Facebook")
    Telegram = fields.Char(string="Telegram")
    Instagram = fields.Char(string="Instagram")
    Viber = fields.Char(string="Viber")
    Skype = fields.Char(string="Skype")

    client_type = fields.Many2one(comodel_name='client.type', string='Client type')
    motives = fields.Many2one(comodel_name='motives', string='Motives')
    services = fields.Char(string="Services", help="What does company really do?")

    what_is_important = fields.Char(string="What is important?")
    what_is_important_consult = fields.Char(string="What is important consult?")
    what_departments = fields.Char(string="What departments?")
    what_is_your_CMS = fields.Many2one(comodel_name='what.is.your.cms', string="What is your CMS?")
    use_in_work = fields.Many2one(comodel_name='use.in.work', string="Use in work")
    receive_a_Leads = fields.Many2one(comodel_name='receive.leads', string="Receive a Leads")
    how_are_bp_described = fields.Char(string="How are bp described?")

    recommendation_from = fields.Many2one(comodel_name='res.partner', string="Recommendation from")
    bonus_for_recom = fields.Many2one(comodel_name='bonus.for.recom', string="Bonus for recommendation")
    special_conditions = fields.Char(string="Special conditions")

    comment_to_payment = fields.Char(string="Comment to payment")
    payment_method = fields.Many2one(comodel_name='payment.method', string="Payment method")
    form_of_payment = fields.Many2one(comodel_name='form.payment', string="Form of payment")
    client_bonus = fields.Char(string="Client bonus", help="'-' if not available")

    process_architecture = fields.Char(string="Process architecture", help="Camunda")
    video_meeting = fields.Char(string="Video meeting")
    good_hour = fields.Char(string="Good hour", help="'-' if not available")
    commercial_offer = fields.Char(string="Commercial offer", help="'-' if not available")

    partner_type = fields.Many2one(comodel_name='partner', string="Partner type")
    what_services = fields.Char(string="What services?")
    referral_suffix = fields.Char(string="Referral suffix")
    referral_link = fields.Char(string="Referral link")

    portal_address = fields.Char(string="Portal address")
    license_key = fields.Char(string="License key")

    cooper_term = fields.Many2one(comodel_name='cooper.term', string="Cooper term")
    license_start_date = fields.Date(string="License start date")
    license_end_date = fields.Date(string="License end date")
    next_opportunity = fields.Many2one(comodel_name='next.opportunity', string="Next opportunity")
    date_next_contract = fields.Date(string="Date next contract")
    strategy = fields.Char(string="Strategy")
    contact_link = fields.Char(string="Contact link")
