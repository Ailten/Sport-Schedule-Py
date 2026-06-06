
window.addEventListener('load', _ => {

    // event to actualise page (by endpoint), when change value of month input.
    Array.prototype.forEach.call(
        document.querySelectorAll('#month-picker, #year-picker'),
        selectPicker => {

            selectPicker.addEventListener('change', (evnt) => {

                month = document.getElementById('month-picker').value;
                month = (month < 10? '0': '') + month;
                year = document.getElementById('year-picker').value;
                document.getElementById('month_ask').value = (`${year}-${month}`);
                document.getElementById('form-actualise-schedule').submit();

            });

        }
    );

    // event to check all exercice from calendar.
    Array.prototype.forEach.call(
        document.querySelectorAll('*.check-whole-day, *.details-whole-day'),
        iCheck => {

            iCheck.addEventListener('click', (evnt) => {
        
                let form = evnt.target;
                do {
                    form = form.parentNode;
                } while(form.tagName.toLowerCase() != 'form');
        
                form.submit();
        
            });
        }
    )
    
});