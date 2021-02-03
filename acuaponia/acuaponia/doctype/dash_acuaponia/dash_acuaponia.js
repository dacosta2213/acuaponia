// Copyright (c) 2048, CODIGO BINARIO and contributors
// For license information, please see license.txt

frappe.ui.form.on('Dash Acuaponia', {
	contenedor: function(frm) {
		frappe.call({
				method: "frappe.client.get",
				args: {
					doctype: "Warehouse",
					filters: {
					"name": cur_frm.doc.contenedor
					}
				},
				callback: function (data) {
					if (frm.doc.__unsaved)  {
						v = data.message;
						console.log(v);
						cur_frm.set_value("field1", v.field1);
						cur_frm.set_value("field2", v.field2);
						cur_frm.set_value("field3", v.field3);
						cur_frm.set_value("field4", v.field4);
						cur_frm.set_value("min1", v.min1);
						cur_frm.set_value("min2", v.min2);
						cur_frm.set_value("min3", v.min3);
						cur_frm.set_value("min4", v.min4);
						cur_frm.set_value("max1", v.max1);
						cur_frm.set_value("max2", v.max2);
						cur_frm.set_value("max3", v.max3);
						cur_frm.set_value("max4", v.max4);

					}
				},
				freeze: true,
				freeze_message: "Cargando Datos"
				})



	},
	refresh: function(frm) {
		// if (cur_frm.doc.doctype = "Dash Acuaponia") {
		// 	setInterval(function() {
		// 	  cur_frm.reload_doc();
		// 		console.log('actualizo dash');
		// 	}, 60000);
		//
		// 	setInterval(function() {
		// 	  location.reload();
		// 		console.log('RECARGA el dash');
		// 	}, 180000);
    // }

		frappe.call({
			method: "acuaponia.acuaponia.doctype.dash_acuaponia.dash_acuaponia.datos",
			args: {
				contenedor: cur_frm.doc.contenedor
			},
			callback: function (r) {
				let results = r.message || [];
				let resultados = results.slice(0, 10);

				let field1 = {
					parent: '.field1',
					title: cur_frm.doc.field1,
					// subtitle:"Los valores normales varían entre 90 y 130 mmHg",
					data: {
						datasets: [ { values: resultados.map(d=>d.field1) } ],
						specific_values : [
							{
								title: 'MIN',
								line_type: "dashed",
								value: cur_frm.doc.min1
							},
							{
								title: 'MAX',
								line_type: "dashed",
								value: cur_frm.doc.max1
							},
						],
						labels: resultados.map(d=>d.creation)
					},
					colors: ['#ffd967'],
					type: 'line', // or 'bar', 'line', 'pie', 'percentage', 'scatter'
					height: 250
				};
				new Chart(field1);

				let field2 = {
					parent: '.field2',
					title: cur_frm.doc.field2,
					// subtitle:"Los valores normales varían entre 90 y 130 mmHg",
					data: {
						datasets: [ { values: resultados.map(d=>d.field2) } ],
						specific_values : [
							{
								title: 'MIN',
								line_type: "dashed",
								value: cur_frm.doc.min2
							},
							{
								title: 'MAX',
								line_type: "dashed",
								value: cur_frm.doc.max2
							},
						],
						labels: resultados.map(d=>d.creation)
					},
					colors: ['blue'],
					type: 'line', // or 'bar', 'line', 'pie', 'percentage', 'scatter'
					height: 250
				};
				new Chart(field2);

				let field3 = {
					parent: '.field3',
					title: cur_frm.doc.field3,
					// subtitle:"Los valores normales varían entre 90 y 330 mmHg",
					data: {
						datasets: [ { values: resultados.map(d=>d.field3) } ],
						specific_values : [
							{
								title: 'MIN',
								line_type: "dashed",
								value: cur_frm.doc.min3
							},
							{
								title: 'MAX',
								line_type: "dashed",
								value: cur_frm.doc.max3
							},
						],
						labels: resultados.map(d=>d.creation)
					},
					colors: ['#ff5858'],
					type: 'line', // or 'bar', 'line', 'pie', 'percentage', 'scatter'
					height: 250
				};
				new Chart(field3);

				let field4 = {
					parent: '.field4',
					title: cur_frm.doc.field4,
					// subtitle:"Los valores normales varían entre 90 y 430 mmHg",
					data: {
						datasets: [ { values: resultados.map(d=>d.field4) } ],
						specific_values : [
							{
								title: 'MIN',
								line_type: "dashed",
								value: cur_frm.doc.min4
							},
							{
								title: 'MAX',
								line_type: "dashed",
								value: cur_frm.doc.max4
							},
						],
						labels: resultados.map(d=>d.creation)
					},
					colors: ['#98d85b'],
					type: 'line', // or 'bar', 'line', 'pie', 'percentage', 'scatter'
					height: 250
				};
				new Chart(field4);
			}
		});

	}
});
