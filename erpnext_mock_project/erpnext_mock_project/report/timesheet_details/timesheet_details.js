// Copyright (c) 2022, Anisha Raulo and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Timesheet Details"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd":1,
			"width": "80", 
			"default": frappe.datetime.add_months(frappe.datetime.get_today(),-1),
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"reqd":1,
			"width": "80", 
			"default": frappe.datetime.add_months(frappe.datetime.get_today(),-1),
		}, 
		{
			"fieldname":"employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options" : "Employee",
			"width": "80",
			"reqd": 0
		},      
		{
			"fieldname":"shift_type",
			"label": __("Shift Type"),
			"fieldtype": "Link",
			"options" : "Shift Type",
			"width": "80",
			"reqd": 0
		},

	]
};
