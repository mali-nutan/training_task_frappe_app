frappe.ui.form.on('Article', {
    onload: function(frm) {
        console.log("Testing for Overriding");
        if (frm.doc.status === 'Issued') {
            frappe.msgprint("Status is issued");
            let currentDate = new Date();
            console.log("Current Date is ", currentDate);
            let issuedDate = new Date(frm.doc.date);
            console.log("Issued Date is ", issuedDate);
            let timeDiff = currentDate.getTime() - issuedDate.getTime();
            let resultDate = Math.floor(timeDiff / (1000 * 3600 * 24));
            console.log("Number of days since the item was issued: ",resultDate);

            frm.set_value('date', frappe.datetime.now_datetime());
            frappe.msgprint("Number of days since the item was issued: " + resultDate + " days");
            console.log("Date is updated successfully");
        }
    }
});
