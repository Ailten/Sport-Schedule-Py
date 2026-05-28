

async function checkAnExo(target) {

    // button already pressed (cooldown fetch).
    if(target.hasAttribute('cooldown-fetch')){
        return;
    }

    let exerciceContainer = target;
    do {
        exerciceContainer = exerciceContainer.parentNode;
    } while(! exerciceContainer.classList.contains('exercice-to-do-container'));

    let dateAsk = document.getElementById('date-ask').value;

    let checkExerciceFormDto = {
        id_exo_to_do: Number(exerciceContainer.getAttribute('index-exo-to-do')),
        date_exo: dateAsk,  // TODO: Cast Date.  // Date.parse(dateAsk)  .toISOString()  new Date(dateAskArr[0], dateAskArr[1], dateAskArr[2])
        date_checked: new Date().toISOString() //new Date()
    }
    
    // make cooldown button (durring fetch call).
    target.setAttribute('cooldown-fetch', 'true');

    await fetch('http://localhost:8000/checkExercice/checkAnExo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(checkExerciceFormDto)
    }).then(response => {
        if (!response.ok) {
            console.error(response);
            throw new Error('error request.');
        }
        return response.json();
    }).then(data => {

        if(data.is_success){
            // mark the exercice to do as checked.
            exerciceContainer.classList.add('exercice-to-do-checked');
        }else{
            if(data.redirect_url !== undefined){
                window.location.href = data.redirect_url;
            }
        }

    }).catch(err => {
        // todo: pop up error.
        return;
    });

    // release cooldown button.
    target.removeAttribute('cooldown-fetch');

}
