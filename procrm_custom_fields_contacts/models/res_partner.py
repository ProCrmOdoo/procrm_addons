from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    traffic_source = fields.Many2one(
        comodel_name="traffic.source", string="Traffic source"
    )
    more_source = fields.Char(string="More source")
    Facebook = fields.Char(string="Facebook")
    Telegram = fields.Char(string="Telegram")
    Instagram = fields.Char(string="Instagram")
    Viber = fields.Char(string="Viber")
    Skype = fields.Char(string="Skype")

    # Basic Information
    # Potential
    client_type = fields.Many2one(comodel_name="client.type", string="Client type")
    motives = fields.Many2many(comodel_name="motives", string="Motives")
    services = fields.Char(string="Services", help="What does company really do?")
    # Neded
    what_departments = fields.Many2many(
        comodel_name="what.departments", string="What departments?"
    )
    departments_other = fields.Text(string="What departments (Other)?")
    what_is_your_CMS = fields.Many2many(
        comodel_name="what.is.your.cms", string="What is your CMS?"
    )
    use_in_work = fields.Many2many(comodel_name="use.in.work", string="Use in work")
    use_in_work_other = fields.Text(string="Use in work - other")
    how_are_bp_described = fields.Char(string="How are bp described")
    receive_a_Leads = fields.Many2many(
        comodel_name="receive.leads", string="Receive a Leads"
    )
    receive_a_Leads_other = fields.Text(string="Receive a leads - other")
    what_is_important = fields.Many2many(
        comodel_name="what.is.important", string="What is important?"
    )
    what_is_important_other = fields.Text(string="What is important? - Other")
    number_of_users = fields.Char(string="How many users are planned?")
    what_is_important_consult = fields.Text(string="What is important consult?")
    # License
    license_now = fields.Many2many(comodel_name="license.now", string="License now")
    license_buy = fields.Many2many(comodel_name="license.buy", string="License buy")
    license_start_date = fields.Date(string="License start date")
    license_end_date = fields.Date(string="License end date")
    portal_address = fields.Many2many(
        comodel_name="portal.address", string="Portal address"
    )  # множине посилання?
    license_key = fields.Text(string="License key")
    # Payment
    cooper_term = fields.Many2many(comodel_name="cooper.term", string="Cooper term")
    # Document
    process_architecture = fields.Char(string="Process architecture", help="Camunda")
    video_meeting = fields.Char(string="Video meeting")
    good_hour = fields.Char(string="Good hour", help="'-' if not available")
    commercial_offer = fields.Char(
        string="Commercial offer", help="'-' if not available"
    )

    # Additional Info
    # Partner
    partner_type = fields.Many2one(comodel_name="partner", string="Partner type")
    what_services = fields.Many2many(
        comodel_name="what.services", string="What services?"
    )
    referral_suffix = fields.Char(string="Referral suffix")
    referral_link = fields.Char(string="Referral link")
    promo_code = fields.Char(string="Promo code")
    # Recomendation
    recommendation_from = fields.Many2one(
        comodel_name="res.partner", string="Recommendation from"
    )
    bonus_for_recom = fields.Many2one(
        comodel_name="bonus.for.recom", string="Bonus for recom"
    )
    special_conditions = fields.Text(string="Special conditions")
    # Control
    #
    date_next_contract = fields.Date(string="Date next contract")
    strategy = fields.Char(string="Strategy")
    contact_link = fields.Char(string="Contact link")
