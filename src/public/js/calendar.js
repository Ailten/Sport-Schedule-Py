
window.addEventListener('load', _ => {

    // event to actualise page (by endpoint), when change value of month input.
    document.getElementById('month-picker').addEventListener('change', (evnt) => {

        document.getElementById('form-actualise-schedule').submit();

    });

    // event to check all exercice from calendar.
    Array.prototype.forEach.call(
        document.getElementsByClassName('check-whole-day'),
        iCheck => {
            iCheck.addEventListener('click', (evnt) => {

                //let dayOfMonth = evnt.target.getAttribute('day-of-month');
                //let month = document.getElementById('month-picker').value;
                //let dateExo = `${month}-${dayOfMonth}`;
                //console.log(dateExo)
        
                let form = evnt.target;
                do {
                    form = form.parentNode;
                } while(form.tagName.toLowerCase() != 'form');
        
                //let input = form.appendChild(document.createElement('input'));
                //input.setAttribute('type', 'date');
                //input.setAttribute('name', 'date_exo');
                //input.setAttribute('value', dateExo);

                //form.querySelector('input[name=date_exo]').setAttribute('value', dateExo);
        
                form.submit();
        
            });
        }
    )
    
});