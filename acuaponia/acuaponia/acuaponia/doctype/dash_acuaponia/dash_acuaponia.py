# -*- coding: utf-8 -*-
# Copyright (c) 2018, CODIGO BINARIO and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DashAcuaponia(Document):
	pass

@frappe.whitelist(allow_guest=True)
def datos(contenedor):
	items = []
	filters = {"contenedor": contenedor }
	x = frappe.get_list("Lectura", fields=["creation","field1","field2","field3","field4"], order_by="creation asc",filters=filters)
	# frappe.errprint(x)
	for val in x:
		# frappe.errprint(val)
		item_obj = {"creation": val.creation,
		"field1": val.field1,
		"field2": val.field2,
		"field3": val.field3,
		"field4": val.field4 }
		items.append(item_obj)

	return items
