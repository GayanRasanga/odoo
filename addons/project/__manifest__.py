# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Project',
    'version': '1.2',
    'website': 'https://www.odoo.com/app/project',
    'category': 'Services/Project',
    'sequence': 45,
    'summary': 'Organize and plan your projects',
    'depends': [
        'analytic',
        'base_setup',
        'mail',
        'portal',
        'rating',
        'resource',
        'web',
        'web_tour',
        'digest',
    ],
    'data': [
        'security/project_security.xml',
        'security/ir.model.access.csv',
        'security/ir.model.access.xml',
        'data/digest_data.xml',
        'data/ir_actions_client_data.xml',
        'report/project_task_burndown_chart_report_views.xml',
        'views/account_analytic_account_views.xml',
        'views/digest_digest_views.xml',
        'views/rating_rating_views.xml',
        'views/project_update_views.xml',
        'views/project_update_templates.xml',
        'views/project_project_stage_views.xml',
        'wizard/project_share_wizard_views.xml',
        'views/project_collaborator_views.xml',
        'views/project_task_type_views.xml',
        'views/project_project_views.xml',
        'views/project_task_views.xml',
        'views/project_tags_views.xml',
        'views/project_milestone_views.xml',
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
        'views/mail_activity_type_views.xml',
        'views/project_sharing_project_task_views.xml',
        'views/project_portal_project_project_templates.xml',
        'views/project_portal_project_task_templates.xml',
        'views/project_task_templates.xml',
        'views/project_sharing_project_task_templates.xml',
        'report/project_report_views.xml',
        'data/ir_cron_data.xml',
        'data/mail_message_subtype_data.xml',
        'data/mail_template_data.xml',
        'data/project_data.xml',
        'wizard/project_task_type_delete_views.xml',
        'wizard/project_project_stage_delete_views.xml',
        'views/project_menus.xml',
    ],
    'demo': [
        'data/mail_template_demo.xml',
        'data/project_demo.xml',
    ],
    'installable': True,
    'application': True,
    'post_init_hook': '_project_post_init',
    'assets': {
        'web.assets_backend': [
            'project/static/src/css/project.css',
            'project/static/src/utils/**/*',
            'project/static/src/components/**/*',
            'project/static/src/views/**/*',
            'project/static/src/js/project_graph_view.js',
            'project/static/src/js/project_pivot_view.js',
            'project/static/src/js/project_rating_graph_view.js',
            'project/static/src/js/project_rating_pivot_view.js',
            'project/static/src/js/project_task_kanban_examples.js',
            'project/static/src/js/tours/project.js',
            'project/static/src/scss/project_dashboard.scss',
            'project/static/src/scss/project_form.scss',
            'project/static/src/scss/project_widgets.scss',
            'project/static/src/xml/**/*',
        ],
        'web.assets_frontend': [
            'project/static/src/scss/portal_rating.scss',
            'project/static/src/scss/project_sharing_frontend.scss',
            'project/static/src/js/portal_rating.js',
        ],
        'web.qunit_suite_tests': [
            'project/static/tests/**/*.js',
        ],
        'web.assets_tests': [
            'project/static/tests/tours/**/*',
            'project/static/tests/views/**/*',
        ],
        'project.webclient': [
            ('include', 'web._assets_helpers'),
            ('include', 'web._assets_backend_helpers'),

            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',

            ('include', 'web._assets_bootstrap_backend'),

            'base/static/src/css/modules.css',

            'web/static/src/core/utils/transitions.scss',
            'web/static/src/core/**/*',
            'web/static/src/search/**/*',
            'web/static/src/webclient/icons.scss', # variables required in list_controller.scss
            'web/static/src/views/*.js',
            'web/static/src/views/*.xml',
            'web/static/src/views/*.scss',
            'web/static/src/views/fields/**/*',
            'web/static/src/views/form/**/*',
            'web/static/src/views/kanban/**/*',
            'web/static/src/views/list/**/*',
            'web/static/src/views/view_button/**/*',
            'web/static/src/views/view_components/**/*',
            'web/static/src/views/view_dialogs/**/*',
            'web/static/src/views/widgets/**/*',
            'web/static/src/webclient/**/*',
            ('remove', 'web/static/src/webclient/navbar/navbar.scss'),  # already in assets_common
            ('remove', 'web/static/src/webclient/clickbot/clickbot.js'), # lazy loaded
            ('remove', 'web/static/src/views/form/button_box/*.scss'),

            # remove the report code and whitelist only what's needed
            ('remove', 'web/static/src/webclient/actions/reports/**/*'),
            'web/static/src/webclient/actions/reports/*.js',
            'web/static/src/webclient/actions/reports/*.xml',

            'web/static/src/env.js',

            'web/static/lib/jquery.scrollTo/jquery.scrollTo.js',
            'web/static/lib/py.js/lib/py.js',
            'web/static/lib/py.js/lib/py_extras.js',
            'web/static/lib/jquery.ba-bbq/jquery.ba-bbq.js',

            'web/static/src/legacy/scss/fields.scss',
            'web/static/src/legacy/scss/views.scss',

            'base/static/src/scss/res_partner.scss',

            # Form style should be computed before
            'web/static/src/views/form/button_box/*.scss',

            'web/static/src/legacy/action_adapters.js',
            'web/static/src/legacy/legacy_service_provider.js',
            'web/static/src/legacy/legacy_client_actions.js',
            'web/static/src/legacy/legacy_dialog.js',
            'web/static/src/legacy/legacy_load_views.js',
            'web/static/src/legacy/legacy_promise_error_handler.js',
            'web/static/src/legacy/legacy_rpc_error_handler.js',
            'web/static/src/legacy/root_widget.js',
            'web/static/src/legacy/legacy_setup.js',
            'web/static/src/legacy/root_widget.js',
            'web/static/src/legacy/backend_utils.js',
            'web/static/src/legacy/utils.js',
            'web/static/src/legacy/pseudo_web_client.js',
            'web/static/src/legacy/web_client.js',
            'web/static/src/legacy/js/chrome/*',
            'web/static/src/legacy/js/components/*',
            'web/static/src/legacy/js/control_panel/*',
            'web/static/src/legacy/js/core/domain.js',
            'web/static/src/legacy/js/core/mvc.js',
            'web/static/src/legacy/js/core/py_utils.js',
            'web/static/src/legacy/js/core/context.js',
            'web/static/src/legacy/js/core/misc.js',
            'web/static/src/legacy/js/fields/abstract_field.js',
            'web/static/src/legacy/js/fields/basic_fields.js',
            'web/static/src/legacy/js/fields/field_utils.js',
            'web/static/src/legacy/js/fields/relational_fields.js',
            'web/static/src/legacy/js/fields/field_registry.js',
            'web/static/src/legacy/js/fields/field_registration.js',
            'web/static/src/legacy/js/fields/field_utils.js',
            'web/static/src/legacy/js/views/abstract_model.js',
            'web/static/src/legacy/js/views/basic/basic_model.js',
            'web/static/src/legacy/js/views/view_utils.js',
            'web/static/src/legacy/js/services/data_manager.js',
            'web/static/src/legacy/js/services/session.js',
            'web/static/src/legacy/js/tools/tools.js',
            'web/static/src/legacy/js/views/**/*',
            'web/static/src/legacy/js/widgets/date_picker.js',
            'web/static/src/legacy/js/widgets/domain_selector_dialog.js',
            'web/static/src/legacy/js/widgets/domain_selector.js',
            'web/static/src/legacy/js/widgets/model_field_selector.js',
            'web/static/src/legacy/js/widgets/model_field_selector_popover.js',
            'web/static/src/legacy/js/env.js',
            'web/static/src/legacy/js/owl_compatibility.js',

            'web_editor/static/src/components/**/*',
            'web_editor/static/src/scss/web_editor.common.scss',
            'web_editor/static/src/scss/web_editor.backend.scss',

            'web_editor/static/src/js/wysiwyg/dialog.js',
            'web_editor/static/src/js/frontend/loader.js',
            'web_editor/static/src/js/backend/**/*',
            'web_editor/static/src/xml/backend.xml',

            'mail/static/src/scss/variables/*.scss',
            'mail/static/src/views/web/form/form_renderer.scss',

            'project/static/src/components/project_task_name_with_subtask_count_char_field/*',
            'project/static/src/components/project_task_state_selection/*',
            'project/static/src/components/project_private_task_many2one_field/*',
            'partner_autocomplete/static/src/js/partner_autocomplete_core.js',
            'partner_autocomplete/static/src/js/partner_autocomplete_many2one.js',
            'partner_autocomplete/static/src/xml/partner_autocomplete.xml',
            'project/static/src/views/project_task_form/*.scss',

            'project/static/src/project_sharing/search/favorite_menu/custom_favorite_item.xml',
            'project/static/src/project_sharing/**/*',
            'web/static/src/start.js',
            'web/static/src/legacy/legacy_setup.js',
        ],
    },
    'license': 'LGPL-3',
}
