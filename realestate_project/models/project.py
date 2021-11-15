# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, SUPERUSER_ID, _
import logging

_logger = logging.getLogger(__name__)

class RealestateProject(models.Model):

    _name = 'realestate.project'


    name = fields.Char(string="ID")
    name_project = fields.Char(string="Name")
    number_units= fields.Integer(String="Number of units")
    resp_empl = fields.Many2one('res.partner' ,string="Responsible")
    unit_ids = fields.One2many('realestate.units','project_id',string="Units")

    # @api.model
    # def create(self, values):
    #     appartments = self.env['product.template']
    #     _logger.warn('PPPPPPPPPPPPPPPPPPPPPPPPPP:')
    #     _logger.warn(values)
    #     views= []
    #     if 'product_ids' in values.keys():
    #         for product in values['product_ids']:
    #             _logger.warn('++++++mmmmm+++++++')
    #             _logger.warn(product[2]['product_id'])
    #             p = appartments.search([('id', '=',product[2]['product_id'])])
    #             _logger.warn(p.name)
    #             p.write({'attachment_ids':values['attachment_ids'],
    #                       'attachment_catalog_ids':values['attachment_catalog_ids'],
    #                       'deed_type':values['deed_type'],
    #                       'nationality_valid':values['good_nationality'],
    #                       'residence_valid':values['residence_valid'],
    #                       'invest_valid':values['invest_valid'],
    #                       'invest_return':values['invest_return'],
    #                       'handover':values['handover'],
    #                       'handover_date':values['handover_date'],
    #                       'payment_method':values['payment_method'],
    #                       'inst_term':values['inst_term'],
    #                       'disc_term':values['disc_term'],
    #                       'project_state':values['project_state'],
    #                       'currency':values['currency'],
    #                       'location':values['location'],
    #                       'town':values['town'],
    #                       'special_requestes':values['special_requestes'],
    #                       'view':values['view'],
    #                       'service_style':values['service_style'],
    #                       'metro_name':values['metro_name'],
    #                       'metro_min':values['metro_min'],
    #                       'metro_km':values['metro_km'],
    #                       'project_type':values['project_type'],
    #                       'metropolice_name':values['metropolice_name'],
    #                       'metropolice_min':values['metropolice_min'],
    #                       'metropolice_km':values['metropolice_km'],
    #                       'airport_min':values['airport_min'],
    #                       'airport_km':values['airport_km'],
    #                       'istanbul_mol_min':values['istanbul_mol_min'],
    #                       'istanbul_mol_km':values['istanbul_mol_km'],
    #                       'mol_name':values['mol_name'],
    #                       'mol_min':values['mol_min'],
    #                       'mol_km':values['mol_km'],
    #                       'downtown_min':values['downtown_min'],
    #                       'downtown_km':values['downtown_km'],
    #                       'highway_min':values['highway_min'],
    #                       'highway_name':values['highway_name'],
    #                       'highway_km':values['highway_km'],
    #                       'univ_name':values['univ_name'],
    #                       'univ_min':values['univ_min'],
    #                       'univ_km':values['univ_km'],
    #                       'hosp_name':values['hosp_name'],
    #                       'hosp_min':values['hosp_min'],
    #                       'hosp_km':values['hosp_km'],
    #                       'school_name':values['school_name'],
    #                       'school_min':values['school_min'],
    #                       'school_km':values['school_km'],
    #                       'other_trans_name':values['other_trans_name'],
    #                       'other_trans_min':values['other_trans_min'],
    #                       'other_trans_km':values['other_trans_km'],
    #                       })

    #     result = super(ProjectProperty, self).create(values)
    #     return result

    # def write(self, values):
    #     appartments = self.env['product.template']
    #     views= []
    #     _logger.warn('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')

    #     _logger.warn(values)
    #     if 'product_ids' in values.keys():
    #         for product in values['product_ids']:
    #             _logger.warn('++++++++++++++++++++Product_ids++++++++++++++++++++++++++')
    #             _logger.warn(product)
    #             val = product[2]
    #             if val != 0 :
    #                 _logger.warn('=====================VAL not 0=====================')
    #                 if 'product_id' in val.keys() :
    #                     _logger.warn('________________product_id in key ______________')
    #                     p = appartments.search([('id', '=',product[2]['product_id'])])
    #                     _logger.warn('@@@@@@@@@@@@@@@@------@@@@@@@@@@@@@@@@')
    #                     if 'attachment_ids' in values.keys():
    #                         p.write({'attachment_ids':values['attachment_ids'],})
    #                     else:
    #                         p.write({'attachment_ids':[attachment.id for attachment in self.attachment_ids]})

    #                     if 'attachment_catalog_ids' in values.keys():
    #                         p.write({'attachment_catalog_ids':values['attachment_catalog_ids'],})
    #                     else:
    #                         p.write({'attachment_catalog_ids':[attachment.id for attachment in self.attachment_catalog_ids]})

    #                     if 'good_nationality' in values.keys():
    #                         p.write({'nationality_valid':values['good_nationality']})
    #                     else:
    #                         p.write({'nationality_valid':self.good_nationality})

    #                     if 'deed_type' in values.keys():
    #                         p.write({'deed_type':values['deed_type']})
    #                     else:
    #                         p.write({'deed_type':self.deed_type})

    #                     if 'residence_valid' in values.keys():
    #                         p.write({'residence_valid':values['residence_valid']})
    #                     else:
    #                         p.write({'residence_valid':self.residence_valid})

    #                     if 'invest_valid' in values.keys():
    #                         p.write({'invest_valid':values['invest_valid']})
    #                     else:
    #                         p.write({'invest_valid':self.invest_valid})

    #                     if 'invest_return' in values.keys():
    #                         p.write({'invest_return':values['invest_return']})
    #                     else:
    #                         p.write({'invest_return':self.invest_return})

    #                     if 'project_type' in values.keys():
    #                         p.write({'project_type':values['project_type']})
    #                     else:
    #                         p.write({'project_type':self.project_type})

    #                     if 'handover' in values.keys():
    #                         p.write({'handover':values['handover']})
    #                     else:
    #                         p.write({'handover':self.handover})

    #                     if 'handover_date' in values.keys():
    #                         p.write({'handover_date':values['handover_date']})
    #                     else:
    #                         p.write({'handover_date':self.handover_date})

    #                     if 'payment_method' in values.keys():
    #                         p.write({'payment_method':values['payment_method']})
    #                     else:
    #                         p.write({'payment_method':self.payment_method})

    #                     if 'inst_term' in values.keys():
    #                         p.write({'inst_term':values['inst_term']})
    #                     else:
    #                         p.write({'inst_term':self.inst_term})

    #                     if 'disc_term' in values.keys():
    #                         p.write({'disc_term':values['disc_term']})
    #                     else:
    #                         p.write({'disc_term':self.disc_term})

    #                     if 'project_state' in values.keys():
    #                         p.write({'project_state':values['project_state']})
    #                     else:
    #                         p.write({'project_state':self.project_state})
                            
    #                     if 'currency' in values.keys():
    #                         p.write({'currency':values['currency']})
    #                     else:
    #                         p.write({'currency':self.currency})
                            
    #                     if 'location' in values.keys():
    #                         p.write({'location':values['location']})
    #                     else:
    #                         p.write({'location':self.location})
                            
    #                     if 'town' in values.keys():
    #                         p.write({'town':values['town']})
    #                     else:
    #                         p.write({'town':self.town})
    #                     if 'special_requestes' in values.keys():
    #                         p.write({'special_requestes':values['special_requestes']})
    #                     else:
    #                         p.write({'special_requestes':[sr.id for sr in self.special_requestes]})
                            
    #                     if 'service_style' in values.keys():
    #                         p.write({'service_style':values['service_style']})
    #                     else:
    #                         p.write({'service_style':[ss.id for ss in self.service_style]})

    #                     if 'view' in values.keys():
    #                         p.write({'view':values['view']})
    #                     else:
    #                         p.write({'view':[ss.id for ss in self.view]})
            
    #     # CHANGES MADE BY CHARAF 
    #                     if 'metro_name' in values.keys():
    #                         p.write({'metro_name':values['metro_name']})
    #                     else:
    #                         p.write({'metro_name':self.metro_name})
                            
    #                     if 'metro_min' in values.keys():
    #                         p.write({'metro_min':values['metro_min']})
    #                     else:
    #                         p.write({'metro_min':self.metro_min})
                            
    #                     if 'metro_km' in values.keys():
    #                         p.write({'metro_km':values['metro_km']})
    #                     else:
    #                         p.write({'metro_km':self.metro_km})
                        
    #                     if 'metropolice_name' in values.keys():
    #                         p.write({'metropolice_name':values['metropolice_name']})
    #                     else:
    #                         p.write({'metropolice_name':self.metropolice_name})
                                
    #                     if 'metropolice_min' in values.keys():
    #                         p.write({'metropolice_min':values['metropolice_min']})
    #                     else:
    #                         p.write({'metropolice_min':self.metropolice_min})
                            
    #                     if 'metropolice_km' in values.keys():
    #                         p.write({'metropolice_km':values['metropolice_km']})
    #                     else:
    #                         p.write({'metropolice_km':self.metropolice_km})

    #                     if 'airport_min' in values.keys():
    #                         p.write({'airport_min':values['airport_min']})
    #                     else:
    #                         p.write({'airport_min':self.airport_min})

    #                     if 'airport_km' in values.keys():
    #                         p.write({'airport_km':values['airport_km']})
    #                     else:
    #                         p.write({'airport_km':self.airport_km})

    #                     if 'istanbul_mol_min' in values.keys():
    #                         p.write({'istanbul_mol_min':values['istanbul_mol_min']})
    #                     else:
    #                         p.write({'istanbul_mol_min':self.istanbul_mol_min})

    #                     if 'istanbul_mol_km' in values.keys():
    #                         p.write({'istanbul_mol_km':values['istanbul_mol_km']})
    #                     else:
    #                         p.write({'istanbul_mol_km':self.istanbul_mol_km})

    #                     if 'mol_min' in values.keys():
    #                         p.write({'mol_min':values['mol_min']})
    #                     else:
    #                         p.write({'mol_min':self.mol_min})

    #                     if 'mol_name' in values.keys():
    #                         p.write({'mol_name':values['mol_name']})
    #                     else:
    #                         p.write({'mol_name':self.mol_name})

    #                     if 'mol_km' in values.keys():
    #                         p.write({'mol_km':values['mol_km']})
    #                     else:
    #                         p.write({'mol_km':self.mol_km})

    #                     if 'downtown_min' in values.keys():
    #                         p.write({'downtown_min':values['downtown_min']})
    #                     else:
    #                         p.write({'downtown_min':self.downtown_min})

    #                     if 'downtown_km' in values.keys():
    #                         p.write({'downtown_km':values['downtown_km']})
    #                     else:
    #                         p.write({'downtown_km':self.downtown_km})

    #                     if 'highway_min' in values.keys():
    #                         p.write({'highway_min':values['highway_min']})
    #                     else:
    #                         p.write({'highway_min':self.highway_min})

    #                     if 'highway_name' in values.keys():
    #                         p.write({'highway_name':values['highway_name']})
    #                     else:
    #                         p.write({'highway_name':self.highway_name})

    #                     if 'highway_km' in values.keys():
    #                         p.write({'highway_km':values['highway_km']})
    #                     else:
    #                         p.write({'highway_km':self.highway_km})

    #                     if 'univ_name' in values.keys():
    #                         p.write({'univ_name':values['univ_name']})
    #                     else:
    #                         p.write({'univ_name':self.univ_name})

    #                     if 'univ_min' in values.keys():
    #                         p.write({'univ_min':values['univ_min']})
    #                     else:
    #                         p.write({'univ_min':self.univ_min})
                            
    #                     if 'univ_km' in values.keys():
    #                         p.write({'univ_km':values['univ_km']})
    #                     else:
    #                         p.write({'univ_km':self.univ_km})
                            
    #                     if 'hosp_name' in values.keys():
    #                         p.write({'hosp_name':values['hosp_name']})
    #                     else:
    #                         p.write({'hosp_name':self.hosp_name})
                            
    #                     if 'hosp_min' in values.keys():
    #                         p.write({'hosp_min':values['hosp_min']})
    #                     else:
    #                         p.write({'hosp_min':self.hosp_min})
                            
    #                     if 'hosp_km' in values.keys():
    #                         p.write({'hosp_km':values['hosp_km']})
    #                     else:
    #                         p.write({'hosp_km':self.hosp_km})
                            
    #                     if 'school_name' in values.keys():
    #                         p.write({'school_name':values['school_name']})
    #                     else:
    #                         p.write({'school_name':self.school_name})
                            
    #                     if 'school_min' in values.keys():
    #                         p.write({'school_min':values['school_min']})
    #                     else:
    #                         p.write({'school_min':self.school_min})
                            
    #                     if 'school_km' in values.keys():
    #                         p.write({'school_km':values['school_km']})
    #                     else:
    #                         p.write({'school_km':self.school_km})
                            
    #                     if 'other_trans_name' in values.keys():
    #                         p.write({'other_trans_name':values['other_trans_name']})
    #                     else:
    #                         p.write({'other_trans_name':self.other_trans_name})
                            
    #                     if 'other_trans_min' in values.keys():
    #                         p.write({'other_trans_min':values['other_trans_min']})
    #                     else:
    #                         p.write({'other_trans_min':self.other_trans_min})
                            
    #                     if 'other_trans_km' in values.keys():
    #                         p.write({'other_trans_km':values['other_trans_km']})
    #                     else:
    #                         p.write({'other_trans_km':self.other_trans_km})
                            
      
    #     else:
    #         for p in self.product_ids:
    #             if 'attachment_ids' in values.keys():       
    #                 p.product_id.write({'attachment_ids':values['attachment_ids'],})
    #             if 'attachment_catalog_ids' in values.keys():       
    #                 p.product_id.write({'attachment_catalog_ids':values['attachment_catalog_ids'],})
    #             if 'good_nationality' in values.keys():
    #                 p.product_id.write({'nationality_valid':values['good_nationality']})
    #             if 'residence_valid' in values.keys():
    #                 p.product_id.write({'residence_valid':values['residence_valid']})
    #             if 'invest_valid' in values.keys():
    #                 p.product_id.write({'invest_valid':values['invest_valid']})
    #             if 'invest_return' in values.keys():
    #                 p.product_id.write({'invest_return':values['invest_return']})
    #             if 'handover' in values.keys():
    #                 p.product_id.write({'handover':values['handover']})
    #             if 'handover_date' in values.keys():
    #                 p.product_id.write({'handover_date':values['handover_date']})
    #             if 'payment_method' in values.keys():
    #                 p.product_id.write({'payment_method':values['payment_method']})
    #             if 'inst_term' in values.keys():
    #                 p.product_id.write({'inst_term':values['inst_term']})
    #             if 'disc_term' in values.keys():
    #                 p.product_id.write({'disc_term':values['disc_term']})
    #             if 'project_state' in values.keys():
    #                 p.product_id.write({'project_state':values['project_state']})
    #             if 'currency' in values.keys():
    #                 p.product_id.write({'currency':values['currency']})
    #             if 'location' in values.keys():
    #                 p.product_id.write({'location':values['location']})
    #             if 'town' in values.keys():
    #                 p.product_id.write({'town':values['town']})
    #             if 'special_requestes' in values.keys():
    #                 p.product_id.write({'special_requestes':values['special_requestes']})
    #             if 'service_style' in values.keys():
    #                 p.product_id.write({'service_style':values['service_style']})
    #             if 'project_type' in values.keys():
    #                 p.product_id.write({'project_type':values['project_type']})
    #             if 'view' in values.keys():
    #                 p.product_id.write({'view':values['view']})
                    
    #             if 'metro_name' in values.keys():
    #                 p.product_id.write({'metro_name':values['metro_name']})
    #             if 'metro_min' in values.keys():
    #                 p.product_id.write({'metro_min':values['metro_min']})
    #             if 'metro_km' in values.keys():
    #                 p.product_id.write({'metro_km':values['metro_km']})
    #             if 'metropolice_name' in values.keys():
    #                 p.product_id.write({'metropolice_name':values['metropolice_name']})
    #             if 'metropolice_min' in values.keys():
    #                 p.product_id.write({'metropolice_min':values['metropolice_min']})
    #             if 'metropolice_km' in values.keys():
    #                 p.product_id.write({'metropolice_km':values['metropolice_km']})
    #             if 'metropolice_km' in values.keys():
    #                 p.product_id.write({'metropolice_km':values['metropolice_km']})
    #             if 'airport_min' in values.keys():
    #                 p.product_id.write({'airport_min':values['airport_min']})
    #             if 'airport_km' in values.keys():
    #                 p.product_id.write({'airport_km':values['airport_km']})
    #             if 'istanbul_mol_min' in values.keys():
    #                 p.product_id.write({'istanbul_mol_min':values['istanbul_mol_min']})
    #             if 'istanbul_mol_km' in values.keys():
    #                 p.product_id.write({'istanbul_mol_km':values['istanbul_mol_km']})
    #             if 'mol_min' in values.keys():
    #                 p.product_id.write({'mol_min':values['mol_min']})
    #             if 'mol_name' in values.keys():
    #                 p.product_id.write({'mol_name':values['mol_name']})
    #             if 'mol_km' in values.keys():
    #                 p.product_id.write({'mol_km':values['mol_km']})
    #             if 'downtown_min' in values.keys():
    #                 p.product_id.write({'downtown_min':values['downtown_min']})
    #             if 'downtown_km' in values.keys():
    #                 p.product_id.write({'downtown_km':values['downtown_km']})
    #             if 'highway_min' in values.keys():
    #                 p.product_id.write({'highway_min':values['highway_min']})
    #             if 'highway_name' in values.keys():
    #                 p.product_id.write({'highway_name':values['highway_name']})
    #             if 'highway_km' in values.keys():
    #                 p.product_id.write({'highway_km':values['highway_km']})
    #             if 'univ_name' in values.keys():
    #                 p.product_id.write({'univ_name':values['univ_name']})
    #             if 'univ_min' in values.keys():
    #                 p.product_id.write({'univ_min':values['univ_min']})
    #             if 'univ_km' in values.keys():
    #                 p.product_id.write({'univ_km':values['univ_km']})
    #             if 'hosp_name' in values.keys():
    #                 p.product_id.write({'hosp_name':values['hosp_name']})
    #             if 'hosp_min' in values.keys():
    #                 p.product_id.write({'hosp_min':values['hosp_min']})
    #             if 'hosp_km' in values.keys():
    #                 p.product_id.write({'hosp_km':values['hosp_km']})
    #             if 'school_name' in values.keys():
    #                 p.product_id.write({'school_name':values['school_name']})
    #             if 'school_min' in values.keys():
    #                 p.product_id.write({'school_min':values['school_min']})
    #             if 'school_km' in values.keys():
    #                 p.product_id.write({'school_km':values['school_km']})
    #             if 'other_trans_name' in values.keys():
    #                 p.product_id.write({'other_trans_name':values['other_trans_name']})
    #             if 'other_trans_min' in values.keys():
    #                 p.product_id.write({'other_trans_min':values['other_trans_min']})
    #             if 'other_trans_km' in values.keys():
    #                 p.product_id.write({'other_trans_km':values['other_trans_km']})
    #             if 'deed_type' in values.keys():
    #                 p.product_id.write({'deed_type':values['deed_type']})
    #     # END OF CHANGES MADE BY CHARAF 


    #     result = super(ProjectProperty, self).write(values)
    #     return result




    # def send_project(self):
    #     ''' Opens a wizard to compose an email, with relevant mail template loaded by default '''
    #     self.ensure_one()
    #     template_id = self.env['ir.model.data'].xmlid_to_res_id('realestate_product.mail_template_project', raise_if_not_found=False)
    #     # the_template = self.env['mail.template'].browse(template_id)
    #     template = self.env.ref('mail_template_project', raise_if_not_found=False)
    #     lang = False
    #     if template:
    #         lang = template._render_lang(self.ids)[self.id]
    #     if not lang:
    #         lang = get_lang(self.env).code

    #     _logger.warn('--------------------------------------------------------')
    #     _logger.warn(template_id)
    #     # p =[]
    #     # for project in self.projects:
    #     #     for attachment in project.attachment_ids:
    #     #         p.append(attachment)
        
    #     ctx = dict(
    #         default_model='project.product',
    #         default_res_id=self.id,
    #         # For the sake of consistency we need a default_res_model if
    #         # default_res_id is set. Not renaming default_model as it can
    #         # create many side-effects.
    #         # default_attachment_ids= [(6,0,[pa.id for pa in p])],
    #         default_res_model='project.product',
    #         default_use_template=bool(template_id),
    #         default_template_id=template_id or False,
    #         default_composition_mode='comment',
    #         mark_invoice_as_sent=True,
    #         # custom_layout="mail_template_projects",
    #         # model_description=self.with_context(lang=lang).type_name,
    #         force_email=True
    #     )


    #     return {
    #         'name': _('Send Projects'),
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'mail.compose.message',
    #         'views': [(False, 'form')],
    #         'view_id': False,
    #         'target': 'new',
    #         'context': ctx,
    #     }

