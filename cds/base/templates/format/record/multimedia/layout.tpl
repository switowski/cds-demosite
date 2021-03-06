{#
## This file is part of CDS.
## Copyright (C) 2015 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#}

{%- block header -%}
    <div class="row">
        <div class="col-md-12">
            <div class="page-header">
                <h2>{{ record.get('title.title', '') }} <br />
                <span style="font-weight:normal"><i>{{ record.get('title_parallel.title') }}</i></span>
                </h2>
            </div>
        </div>
    </div>
{%- endblock -%}
{%- block body -%}{%- endblock -%}
{%- block footer -%}{%- endblock -%}
