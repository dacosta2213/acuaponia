# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _
import frappe.utils
import frappe.async
import frappe.sessions
import frappe.utils.file_manager
import frappe.desk.form.run_method
from frappe.utils.response import build_response
import datetime
from datetime import date,datetime
import requests
import json
import pytz


@frappe.whitelist()
def ruta(login_manager):
    ruta = frappe.db.get_value("User", login_manager.user,"ruta_login")
    frappe.errprint(ruta)
    frappe.local.response["home_page"] = ruta


@frappe.whitelist(allow_guest=True)
def addlectura(apikey=None,field1=0,field2=0,field3=0,field4=0):
    """Agregar Lectura"""
    tz = pytz.timezone('US/Central')
    now = datetime.now(tz)
    frappe.db.sql("insert into tabLectura (name,creation,field1,field2,field3,field4,contenedor) values (%s,%s,%s,%s,%s,%s,%s)", (now,now,field1,field2,field3,field4,apikey))
    frappe.db.commit()
    # obtener maximos y minimos para las alertas
    cont = frappe.get_doc("Warehouse", apikey)
    especie = frappe.get_doc("Especie", cont.especie)

    # para field1
    min1 = especie.min1
    max1 = especie.max1
    f1 = float(field1)
    # para field2
    min2 = especie.min2
    max2 = especie.max2
    f2 = float(field2)
    # para field3
    min3 = especie.min3
    max3 = especie.max3
    f3 = float(field3)
    # para field4
    min4 = especie.min4
    max4 = especie.max4
    f4 = float(field4)

    if f1 < min1 or f1 > max1:
        enviarsms(apikey,f1,min1,max1)
        enviarmail(apikey,f1,min1,max1)
        return('ALERTA - Lectura fuera de rango: ' + str(f1) + '. MIN: ' + str(min1) + ' MAX: ' + str(max1) )

    elif f2 < min2 or f2 > max2:
        enviarsms(apikey,f2,min2,max2)
        enviarmail(apikey,f2,min2,max2)
        return('ALERTA - Lectura fuera de rango: ' + str(f2) + '. MIN: ' + str(min2) + ' MAX: ' + str(max2) )

    elif f3 < min3 or f3 > max3:
        enviarsms(apikey,f3,min3,max3)
        enviarmail(apikey,f3,min3,max3)
        return('ALERTA - Lectura fuera de rango: ' + str(f3) + '. MIN: ' + str(min3) + ' MAX: ' + str(max3) )

    elif f4 < min4 or f4 > max4:
        enviarsms(apikey,f4,min4,max4)
        enviarmail(apikey,f4,min4,max4)
        return('ALERTA - Lectura fuera de rango: ' + str(f4) + '. MIN: ' + str(min4) + ' MAX: ' + str(max4) )

    else :
        return('Lectura en rango.')


@frappe.whitelist()
def enviarsms(contenedor,f1,min1,max1):
    d = frappe.get_doc("Warehouse", contenedor)
    # phone_number = '3323438381'
    phone_number = d.alerta_sms

    c = frappe.get_doc("Defaults Acuaponia", "Defaults Acuaponia")
    token = c.token
    url = c.url
    device_id = c.device_id
    # token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTUzNzIwNDY3NiwiZXhwIjo0MTAyNDQ0ODAwLCJ1aWQiOjQyMjc5LCJyb2xlcyI6WyJST0xFX1VTRVIiXX0.Buch1pLS7OtGx2pFJrRw2bpy4ZJ6VDD6GZeZy03mXKo"
    # device_id = '98001'
    # url = 'https://smsgateway.me/api/v4/message/send'
    message = 'Alerta en contenedor: ' + contenedor + '. Lectura fuera de rango: ' + str(f1) + '. MIN: ' + str(min1) + ' MAX: ' + str(max1)
    payload = '[{ "phone_number": "' + phone_number + '","message": "' + message + '" ,"device_id": "' +  device_id + '" }]'
    headers = {
    'Authorization': token
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    # frappe.errprint(response.text)
    # return response.text


@frappe.whitelist()
def enviarmail(contenedor,f1,min1,max1):
    c = frappe.get_doc("Warehouse", contenedor)
    message = 'Lectura fuera de rango en ' + contenedor + '. Lectura recibida: ' + str(f1) + '. MIN: ' + str(min1) + ' MAX: ' + str(max1)
    frappe.sendmail(["{0}".format(c.alerta_email)], \
    subject="Alerta en:  {0}.".format(contenedor), \
    content=message,delayed=False)
    # pa que me llegue copia a mi
    frappe.sendmail(['soporte@posix.mx'],subject="Enviar SMS",content='activo',delayed=False)
