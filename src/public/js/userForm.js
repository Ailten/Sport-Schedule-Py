
window.addEventListener('load', _ => {

    // set gender from dto reload.
    inputGenderHidden = document.getElementById('gender-from-dto');
    if(inputGenderHidden != null) {
        inputGenderRadio = document.querySelector(`input[name="gender"][value="${inputGenderHidden.value}"]`);
        inputGenderRadio.setAttribute('checked', 'true');
    }

});