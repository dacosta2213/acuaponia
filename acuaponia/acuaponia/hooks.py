# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "acuaponia"
app_title = "Acuaponia"
app_publisher = "CODIGO BINARIO"
app_description = "Acuaponia for Frappe"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "soporte@posix.mx"
app_license = "MIT"

# Includes in <head>
# ------------------
error_report_email = "admin@codigo-binario.com"

# include js, css files in header of desk.html
# RG- Aqui listar cualquier asset adicional y ponerlo en el folder de assets
app_include_css = ["/assets/acuaponia/css/posix.css","/assets/css/sweetalert2.css","/assets/css/modal-video.min.css","/assets/acuaponia/css/app.css",]
app_include_js = ["/assets/js/posix.min.js","/assets/js/sweetalert2.min.js","/assets/acuaponia/js/app.js","/assets/js/modal-video.min.js","/assets/js/fontawesome-all.min.js","/assets/js/charts.min.js",]

# app_include_css = "/assets/acuaponia/css/retail.css"
# app_include_js = "/assets/retail/js/retail.js"
on_session_creation = [
	"acuaponia.api.ruta"
]

# include js, css files in header of web template
web_include_css = "/assets/retail/css/app-web.css"
web_include_js = "/assets/retail/js/app-web.js"

fixtures = [
    "Role",
    "Print Format",
    "UOM",
    "Mode of Payment",
    "Property Setter",
    "Translation",
    "Custom Script",
    "Custom Role",
    "Custom DocPerm",
    "Website Settings",
    "SMS Settings",
    "System Settings",
    "Portal Settings",
    "Role Permission for Page and Report",
    "User Permission for Page and Report",
    "Website Script",
    "Notification Control",
    "Custom Field"
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/acuaponia/css/acuaponia.css"
# app_include_js = "/assets/acuaponia/js/acuaponia.js"

# include js, css files in header of web template
# web_include_css = "/assets/acuaponia/css/acuaponia.css"
# web_include_js = "/assets/acuaponia/js/acuaponia.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "acuaponia.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "acuaponia.install.before_install"
# after_install = "acuaponia.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "acuaponia.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"acuaponia.tasks.all"
# 	],
# 	"daily": [
# 		"acuaponia.tasks.daily"
# 	],
# 	"hourly": [
# 		"acuaponia.tasks.hourly"
# 	],
# 	"weekly": [
# 		"acuaponia.tasks.weekly"
# 	]
# 	"monthly": [
# 		"acuaponia.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "acuaponia.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "acuaponia.event.get_events"
# }
