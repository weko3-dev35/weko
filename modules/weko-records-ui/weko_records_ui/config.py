# -*- coding: utf-8 -*-
#
# This file is part of WEKO3.
# Copyright (C) 2017 National Institute of Informatics.
#
# WEKO3 is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# WEKO3 is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with WEKO3; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.

"""Configuration for weko-records-ui."""

WEKO_RECORDS_UI_DETAIL_TEMPLATE = 'weko_records_ui/detail.html'

RECORDS_UI_ENDPOINTS = dict(
    recid=dict(
        pid_type='recid',
        route="/records/<pid_value>",
        # view_imp='weko_records.fd.weko_view_method',
        template='weko_records_ui/detail.html',
        record_class='weko_deposit.api:WekoRecord',
    ),
    recid_export=dict(
        pid_type='recid',
        route="/records/<pid_value>/export/<format>",
        view_imp='weko_records_ui.views.export',
        template='weko_records_ui/export.html',
        record_class='weko_deposit.api:WekoRecord',
    ),
    recid_files=dict(
        pid_type='recid',
        route='/record/<pid_value>/files/<path:filename>',
        view_imp='weko_records.fd.file_download_ui',
        record_class='weko_deposit.api:WekoRecord',
    ),
    recid_preview=dict(
        pid_type='recid',
        route='/record/<pid_value>/preview/<path:filename>',
        view_imp='invenio_previewer.views.preview',
        record_class='weko_deposit.api:WekoRecord',
    ),
)

RECORDS_UI_EXPORT_FORMATS = {
    'recid': {
        'junii2': dict(
            title='JUNII2',
            serializer='weko_schema_ui.serializers.WekoCommonSchema',
            order=1,
        ),
        'jpcoar': dict(
            title='JPCOAR',
            serializer='weko_schema_ui.serializers.WekoCommonSchema',
            order=2,
        ),
        'dc': dict(
            title='DublinCore',
            serializer='weko_schema_ui.serializers.WekoCommonSchema',
            order=3,
        ),
        'json': dict(
            title='JSON',
            serializer='invenio_records_rest.serializers.json_v1',
            order=4,
        ),
    }
}

OAISERVER_METADATA_FORMATS = {
    'junii2': {
        'serializer': (
            'weko_schema_ui.utils:dumps_oai_etree', {
                'schema_type': "junii2",
            }
        ),
        'schema': 'http://www.openarchives.org/OAI/2.0/oai_dc.xsd',
        'namespace': 'http://www.openarchives.org/OAI/2.0/oai_dc/',
    },
    'jpcoar': {
        'serializer': (
            'weko_schema_ui.utils:dumps_oai_etree', {
                'schema_type': "jpcoar",
            }
        ),
        'namespace': 'https://irdb.nii.ac.jp/schema/jpcoar/1.0/',
        'schema': 'https://irdb.nii.ac.jp/schema/jpcoar/1.0/jpcoar_scm.xsd',
    },
    'oai_dc': {
        'serializer': (
            'weko_schema_ui.utils:dumps_oai_etree', {
                'schema_type': "dc",
            }
        ),
        'namespace': 'http://www.openarchives.org/OAI/2.0/oai_dc/',
        'schema': 'http://www.openarchives.org/OAI/2.0/oai_dc.xsd',
    }
}
