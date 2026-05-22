
window.addEventListener('load', _ => {

    // event to actualise page (by endpoint), when change value of month input.
    document.getElementById('month-picker').addEventListener('change', (evnt) => {

        document.getElementById('form-actualise-schedule').submit()

    });
    
});