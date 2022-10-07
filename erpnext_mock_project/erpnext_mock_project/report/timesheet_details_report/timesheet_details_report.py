# Copyright (c) 2022, Anisha Raulo and contributors
# For license information, please see license.txt

import frappe
from frappe import _
def execute(filters=None):
	conditions= get_conditions(filters)
	columns= get_columns()
	data = get_data(filters,conditions)
	return columns, data

def get_columns():
	columns=[
		    {
               "fieldname":"employee",
               "label":_("Employee"),
               "fieldtype":"Data",
			   "options":"",
               "width":100,
		    },
			{
               "fieldname":"employee_name",
               "label":_("Employee Name"),
               "fieldtype":"Data",
			   "options":"",
               "width":100,
			},
			{
               "fieldname":"no_of_days_in_a_month",
               "label":_("No of Days in a month"),
               "fieldtype":"Data",
			   "width":100,
			},
			{
              "fieldname":"total_working_days",
              "label":_("Total Working Days"),
              "fieldtype":"Data",
			  "width":100,
			},
			{
               "fieldname":"present_days",
               "label":_("Present Days"),
               "fieldtype":"Data",
			   "width":100,
			},
			{
               "fieldname":"absent_days",
               "label":_("Absent Days"),
               "fieldtype":"Data",
			   "options":"Item",
			   "width":100,
			},
			{
               "fieldname":"default_shift",
               "label":_("Default Shift"),
               "fieldtype":"Data",
			   "width":100,
			},
			#{
            #  "fieldname":"no_of_half_days",
            #  "label":_("No of Half Days"),
            #  "fieldtype":"Data",
			#   "width":100,
			#},
	]
	return columns

def get_data(filters,conditions):
	data = frappe.db.sql(f""" select `tabTimesheet`.employee,
	                         `tabTimesheet`.employee_name,
							 `tabTimesheet`.no_of_days_in_a_month, 
							 `tabTimesheet`.total_working_days,
							 `tabTimesheet`.present_days,
							 `tabTimesheet`.absent_days,
							 `tabEmployee`.default_shift,
					          from `tabTimesheet`, `tabEmployee` 
							  where `tabTimesheet`.total_working_days between '{filters.get('from_date')}' and '{filters.get('to_date')}' {conditions} """,as_dict=True)

	return data
def get_conditions(filters):
	conditions = ""
	if filters.get('from_date'):
		conditions += " AND  `tabTimesheet`.total_working_days >'{}'".format(filters.get('from_date'))
	if filters.get('to_date'):
		conditions += " AND  `tabTimesheet`.total_working_days < '{}'".format(filters.get('to_date'))
	return conditions
		