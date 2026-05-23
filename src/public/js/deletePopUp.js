
window.addEventListener('load', _ => {

    // set event click on button del of all pop-up in page.
    popUpDelButton = document.getElementsByClassName('pop-up-error-del-button');
    Array.prototype.forEach.call(
        popUpDelButton,
        (delButton, i) => {

            // get the parent dom who is pop-up.
            let popUp = delButton;
            do{
                popUp = popUp.parentNode;
            }while(!popUp.classList.contains('pop-up-error'));

            // set event click on button del.
            delButton.addEventListener('click', _ => {
                deletePopUp(popUp)
            });


            // remove pop-up after a while.
            reverceIndex = (popUpDelButton.length - i -1);  // get index of popup starting from the bottom one.
            setTimeout(_ => {

                popUp.classList.add('fade-out-delete');  // animation opacity lowered.
                popUp.addEventListener('animationend', (evnt) => {  // remove dom when animation end.
                    deletePopUp(popUp);
                });

            }, 3000 + (reverceIndex * 2000) );  // 3 sec to read it (+2sec by other pop-up).

        }
    );

});


function deletePopUp(popUp) {
    
    // delete pop up dom.
    let popUpContainer = popUp.parentNode;
    popUpContainer.removeChild(popUp);

    // if it's last pop up, remove container also.
    if(popUpContainer.getElementsByClassName('pop-up-error').length == 0) {
        popUpContainer.parentNode.removeChild(popUpContainer);
    }

}