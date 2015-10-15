# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2012, 2013, 2014, 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Statistics Flask Blueprint."""

from flask import Blueprint, g, Markup, render_template, request

from flask_login import login_required

from flask_menu import register_menu

from functools import wraps

# TODO:
# invenio_access is broken, replace it back later
# from invenio_access.engine import acc_authorize_action
acc_authorize_action = lambda x, y: (0, '')

from invenio_base.i18n import _
from invenio_records.utils import visible_collection_tabs
from invenio_records.views import request_record

from .config import STATS_CFG


blueprint = Blueprint(
    'statistics', __name__, url_prefix="/record", template_folder='templates',
    static_folder='static'
)


def viewstatistics_only(f):
    @wraps(f)
    @login_required
    def _wrapped(*args, **kwargs):
        authorized, msg = acc_authorize_action(request, 'viewstatistics')
        if authorized != 0:
            return render_template('visualisations/403.html',
                                   message=Markup(msg)), 403
        return f(*args, **kwargs)
    return _wrapped


@blueprint.route('/<int:recid>/statistics', methods=['GET', 'POST'])
@request_record
@register_menu(blueprint, 'record.statistics', _('Statistics'), order=9,
               endpoint_arguments_constructor=lambda:
               dict(recid=request.view_args.get('recid')),
               # visible_when=visible_collection_tabs('statistics'))
               visible_when=lambda: True)
@viewstatistics_only
def statistics(recid):
    """This function will render the list of available statistics"""
    statistics = []
    for (event_name, event) in STATS_CFG['events'].items():
        event_statistics = STATS_CFG['events'][event_name]['statistics']
        for (statistic_name, statistic) in event_statistics.items():
            statistics.append({
                'name': event['title'] + ' ' + statistic_name,
                'path': blueprint.url_prefix + '/' + str(recid) +
                '/statistics/' + event_name + '/' + statistic_name
            })

    return render_template('statistics/index.html',
                           statistics=statistics)


@blueprint.route('/<int:recid>/statistics/<event_name>/<statistic>',
                 methods=['GET'])
@request_record
@viewstatistics_only
def view_statistic(recid, event_name=None, statistic=None):
    """This function will render statistics for a single event."""

    if event_name not in STATS_CFG['events']:
        # 404
        return 'no such event', 404
    if 'statistics' not in STATS_CFG['events'][event_name]:
        # 404
        return 'no statistics associated with this event', 404
    if statistic not in STATS_CFG['events'][event_name]['statistics']:
        # 404
        return 'no such statistic for this event', 404
    event = STATS_CFG['events'][event_name]
    display = event['statistics'][statistic]['display']
    query_type = event['statistics'][statistic]['query_type']

    data = {
        'recid': recid,
        'doc_type': event_name,
        'statistic_data': event['statistics'][statistic],
        'title': event['title'],
        'query_type': query_type,
    }
    return render_template('statistics/%s.html' % display,
                           data=data)
