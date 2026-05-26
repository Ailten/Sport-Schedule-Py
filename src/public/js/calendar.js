
window.addEventListener('load', _ => {

    // event to actualise page (by endpoint), when change value of month input.
    document.getElementById('month-picker').addEventListener('change', (evnt) => {

        document.getElementById('form-actualise-schedule').submit();

    });

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