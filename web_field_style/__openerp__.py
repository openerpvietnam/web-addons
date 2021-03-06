# -*- coding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2012-2013 Agile Business Group sagl
#    (<http://www.agilebg.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Field Style',
    'version': '1.0',
    'category': 'web',
    'description': """Allows to specify different colors or 
    CSS class per field in view definition.

    Three new attributes will be available on the field element of a view:
        `bgcolor` for setting the background color
        `fgcolor` for setting the foreground color (basically the text)
        `ccsclass` for setting a custom CSS class to be applied on the field

    `bg/fgcolor` are very useful for people that only want to change some field color without
    having to deal with CSS.

    NOTE: you must apply a simple patch to this server's file

        `server/openerp/addons/base/rng/view.rng`

    Just use the patch provided by this module (see server-view.rng.patch in the root of the package).
    
    """,
    'author': 'Agile Business Group & Domsense',
    'website': 'http://www.agilebg.com',
    'license': 'AGPL-3',
    'depends': ['web'],
    'data': [],
    'active': False,
    'installable': True,
    'js': [
        'static/js/web_field_style.js',
    ],
    'qweb': [
        'static/xml/web_field_style.xml',
    ],
    'css': [
        'static/css/fields.css',
    ]
}

