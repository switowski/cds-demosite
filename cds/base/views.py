# -*- coding: utf-8 -*-
##
## This file is part of CDS.
## Copyright (C) 2013, 2014, 2015 CERN.
##
## CDS is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDS; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""CDS Demosite interface."""

from flask import Blueprint
from jinja2 import Template

blueprint = Blueprint(
    'cds', __name__, url_prefix='/', template_folder='templates',
    static_folder='static'
)


# CDS useful template filters
# ===========================
@blueprint.app_template_filter('wrap_with_link')
def wrap_with_link(value, url="#"):
    """Wrap a text with html link."""
    template = Template(
        "<a href='{{ url }}'>{{ value }}</a>"
    )
    data = dict(value=value, url=url)
    return template.render(**data)
