// Copyright (c) 2022, Anisha Raulo and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Deduction', {
//	start_date:function(frm)
//      {
 //     console.log("Employee.............")
   //   Employee=frappe.db.get_value("Employee",employee, "employee_name")
     // frappe.db.set_value('employee_name',Employee)  
     // },
  //deduction_type:function(frm) { 
    //      var end_date = moment(frm.doc.start_date).endOf('month').format('YYYY-MM-DD')
     //     $.each(frm.doc.finance_books || [], function(i, d) {
      //        d.end_date = end_date;
       //       });
        //    refresh_field("deduction_type");
          //  }
    end__date: function(frm,cdt,cdn)
   {   
    $.each(frm.doc.deduction_detail,function(idx,item)
   {
   console.log("......",frappe.datetime.add_months(item.start__date,1))
   if(item.deduction_type=Onetime)
   item.end_date=moment(frm.doc.item.start_date).endOf('month').format('YYYY-MM-DD')
   });
   refresh_field("start_date");
   }
   });

   