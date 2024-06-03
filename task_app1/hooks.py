app_name = "task_app1"
app_title = "Task App1"
app_publisher = "Nutan"
app_description = "Js handeler app for Tutorial app.Part of my training task"
app_email = "nuta@gmail.com"
app_license = "123"
doctype_js = {
    "Article": "public/js/custom_article.js"
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/task_app1/css/task_app1.css"
# app_include_js = "/assets/task_app1/js/task_app1.js"

# include js, css files in header of web template
# web_include_css = "/assets/task_app1/css/task_app1.css"
# web_include_js = "/assets/task_app1/js/task_app1.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "task_app1/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "task_app1.utils.jinja_methods",
# 	"filters": "task_app1.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "task_app1.install.before_install"
# after_install = "task_app1.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "task_app1.uninstall.before_uninstall"
# after_uninstall = "task_app1.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "task_app1.utils.before_app_install"
# after_app_install = "task_app1.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "task_app1.utils.before_app_uninstall"
# after_app_uninstall = "task_app1.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "task_app1.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"task_app1.tasks.all"
# 	],
# 	"daily": [
# 		"task_app1.tasks.daily"
# 	],
# 	"hourly": [
# 		"task_app1.tasks.hourly"
# 	],
# 	"weekly": [
# 		"task_app1.tasks.weekly"
# 	],
# 	"monthly": [
# 		"task_app1.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "task_app1.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "task_app1.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "task_app1.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["task_app1.utils.before_request"]
# after_request = ["task_app1.utils.after_request"]

# Job Events
# ----------
# before_job = ["task_app1.utils.before_job"]
# after_job = ["task_app1.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"task_app1.auth.validate"
# ]
