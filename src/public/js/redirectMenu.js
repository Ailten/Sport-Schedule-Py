
window.addEventListener('load', _ => {

    // set event click on button nav menu.
    Array.prototype.forEach.call(
        document.querySelectorAll('*[redirect-menu]'),
        navButton => {

            // set event click.
            navButton.addEventListener('click', (evnt) => {

                btn = evnt.target;

                // do nothing if it's the current page load.
                if(btn.classList.contains('active')){
                    return;
                }

                // redirect.
                window.location.href = btn.getAttribute('redirect-menu');

            });

        }
    );

});