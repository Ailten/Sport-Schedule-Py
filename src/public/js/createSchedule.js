

window.addEventListener('load', _ => {

    // override submit form create schedule.
    //document.getElementById('form-create-schedule').addEventListener('submit', async (evnt) => {
    document.getElementById('button-submit').addEventListener('click', async (evnt) => {

        // get form.
        currentForm = evnt.target;
        do {
            currentForm = currentForm.parentNode;
        } while(currentForm.tagName.toLowerCase() != 'form');

        // cancel default call of form submit.
        //evnt.preventDefault();

        // re-build parameters of form.
        let exerciceToDos = Object.values(  // cast dict key-obj to list obj.
            Array.from(document.querySelectorAll('*[index-exo]')).map(e => {
                return {
                    exercice_id: e.querySelector('input[name^="hidden-type-exo"]').value,
                    days_of_week: daysWeekEnum[e.querySelector('input[name^="type-exo"]').getAttribute('name').split('-')[2]],
                    repetition: e.querySelector('input[name^="reps"]').value,
                    series: e.querySelector('input[name^="series"]').value,
                    additional_weight: Number(e.querySelector('input[name^="weight"]').value)
                }
            }).reduce((acc, e) => {  // merge values identique on many days distinct.
                let uniqueKeyMerge = `${e.exercice_id}-${e.repetition}-${e.series}-${e.additional_weight}`;
                if(!acc[uniqueKeyMerge]){
                    acc[uniqueKeyMerge] = { ...e };  // add new row with key.
                }else{
                    acc[uniqueKeyMerge].days_of_week += e.days_of_week;  // increase previous row with value of same key.
                }
                return acc;
            }, {})
        );

        // call end point form.
        await fetch(currentForm.getAttribute('data-url-dest'), {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                exercice_to_dos: exerciceToDos
            })
        }).then(response => {
            if (!response.ok) {
                console.error(response);
                throw new Error('error request.');
            }
            return response.json();
        }).then(data => {
            window.location.href = data.redirect_url;
        }).catch(err => {
            // todo: mark pop up error.
            return;
        });

    });

});


function addBlockInputExercice(btnTarget) {

    // get container.
    dayContainer = btnTarget;
    do {
        dayContainer = dayContainer.parentNode;
    } while (! dayContainer.classList.contains('block-day'));
    dayStr = dayContainer.getAttribute('id');

    // let last block in container (to insert before button create).
    lastDomChild = null;
    indexExo = null;
    {
        domChilds = dayContainer.querySelectorAll(':scope > *');
        lastDomChild = domChilds[domChilds.length - 1];
        indexExo = domChilds.length - 1;

        // second check, if this index is already taken (by a previous remove).
        indexSet = Array.from(lastDomChild)
            .filter(e => e.hasAttribute('indexExo'))
            .map(e => e.getAttribute('indexExo'));
        if(indexSet.includes(indexExo)) {
            for(let i=0; true; i++) {
                if(indexSet.includes(i))
                    continue;
                indexExo = i
                break
            }
        }
    }


    // build block inputs exercice-to-do.
    let exerciceToDoContainer = dayContainer.insertBefore(document.createElement('div'), lastDomChild);
    exerciceToDoContainer.classList.add('exercice-to-do-container', 'card', 'card-body', 'mt-2', 'container-exo-card');
    exerciceToDoContainer.setAttribute('index-exo', indexExo);


    // fill block inputs exercice-to-do.
    // remove button.
    {
        let typeExoContainer = exerciceToDoContainer.appendChild(document.createElement('div'));
        typeExoContainer.classList.add('d-flex', 'flex-row-reverse');

        let closeButton = typeExoContainer.appendChild(document.createElement('button'));
        closeButton.setAttribute('type', 'button');
        closeButton.classList.add('btn', 'btn-danger', 'fw-bold');
        let closeButtonIco = closeButton.appendChild(document.createElement('i'));
        closeButtonIco.classList.add('bi', 'bi-x');
        //closeButton.innerText = 'X';

        // event remove.
        closeButton.addEventListener('click', (evnt) => {
            let containerToDel = evnt.target;
            do {
                containerToDel = containerToDel.parentNode;
            } while(! containerToDel.classList.contains('container-exo-card'));
            containerToDel.parentNode.removeChild(containerToDel);  // remove.
        });

    }

    // type exercice.
    {
        let typeExoContainer = exerciceToDoContainer.appendChild(document.createElement('div'));
        let libeleInput = `type-exo-${dayStr}-${indexExo}`;  // make an unique libele

        let labelName = typeExoContainer.appendChild(document.createElement('div'));
        labelName.setAttribute('for', libeleInput);
        labelName.classList.add('form-label', 'text-secondary', 'fs-7');
        labelName.innerText = 'Exercice';

        let input = typeExoContainer.appendChild(document.createElement('input'));
        input.setAttribute('type', 'text');
        input.classList.add('form-control', 'form-control-lg');
        input.setAttribute('id', libeleInput);
        input.setAttribute('name', libeleInput);
        input.setAttribute('list', 'exercice-enum-ref');
        input.setAttribute('required', 'true');
        input.setAttribute('place-holder', 'Pompes');

        // event change on input type exercice, to block value out of enum.
        input.addEventListener('change', (evnt) => {
            let inputEnumExo = evnt.target;
            let valueInput = inputEnumExo.value.toLowerCase();
            let enumMatch = Array.from(document.querySelectorAll('#exercice-enum-ref > *')).map(e => {
                return {
                    value: e.getAttribute('value').toLowerCase(),
                    id: e.getAttribute('data-id-value')
                };
            }).find(e => e.value == valueInput);
            let hiddenInputEnumExo = document.querySelector(`input[name="hidden-type-exo-${dayStr}-${indexExo}"]`);
            
            if (
                (valueInput === "" && inputEnumExo.hasAttribute('required'))  // input empty (when required).
                ||
                enumMatch === undefined  // value not in enum range.
            ) {
                inputEnumExo.classList.add('is-invalid');
                inputEnumExo.classList.remove('is-valid');
                hiddenInputEnumExo.value = '-1';  // reset value hidden.
            } else {  // valide.
                inputEnumExo.classList.add('is-valid');
                inputEnumExo.classList.remove('is-invalid');
                hiddenInputEnumExo.value = enumMatch.id;  // set value hidden.
            }

        });

        let hiddenInput = typeExoContainer.appendChild(document.createElement('input'));
        hiddenInput.setAttribute('type', 'hidden');
        hiddenInput.setAttribute('name', `hidden-type-exo-${dayStr}-${indexExo}`);
        hiddenInput.setAttribute('value', '-1');
    }

    // reps.
    {
        let typeExoContainer = exerciceToDoContainer.appendChild(document.createElement('div'));
        let libeleInput = `reps-${dayStr}-${indexExo}`;  // make an unique libele

        let labelName = typeExoContainer.appendChild(document.createElement('div'));
        labelName.setAttribute('for', libeleInput);
        labelName.classList.add('form-label', 'text-secondary', 'fs-7');
        labelName.innerText = 'Repetitions';

        let input = typeExoContainer.appendChild(document.createElement('input'));
        input.setAttribute('type', 'number');
        input.classList.add('form-control', 'form-control-lg');
        input.setAttribute('id', libeleInput);
        input.setAttribute('name', libeleInput);
        input.setAttribute('required', 'true');
        input.setAttribute('placeholder', '3');
        input.setAttribute('min', '0');
    }

    // series
    {
        let typeExoContainer = exerciceToDoContainer.appendChild(document.createElement('div'));
        let libeleInput = `series-${dayStr}-${indexExo}`;  // make an unique libele

        let labelName = typeExoContainer.appendChild(document.createElement('div'));
        labelName.setAttribute('for', libeleInput);
        labelName.classList.add('form-label', 'text-secondary', 'fs-7');
        labelName.innerText = 'Series';

        let input = typeExoContainer.appendChild(document.createElement('input'));
        input.setAttribute('type', 'number');
        input.classList.add('form-control', 'form-control-lg');
        input.setAttribute('id', libeleInput);
        input.setAttribute('name', libeleInput);
        input.setAttribute('required', 'true');
        input.setAttribute('placeholder', '3');
        input.setAttribute('min', '0');
    }

    // weight.
    {
        let typeExoContainer = exerciceToDoContainer.appendChild(document.createElement('div'));
        let libeleInput = `weight-${dayStr}-${indexExo}`;  // make an unique libele

        let labelName = typeExoContainer.appendChild(document.createElement('div'));
        labelName.setAttribute('for', libeleInput);
        labelName.classList.add('form-label', 'text-secondary', 'fs-7');
        labelName.innerText = 'Weight Add';

        let input = typeExoContainer.appendChild(document.createElement('input'));
        input.setAttribute('type', 'number');
        input.setAttribute('steps', '0.1');
        input.classList.add('form-control', 'form-control-lg');
        input.setAttribute('id', libeleInput);
        input.setAttribute('name', libeleInput);
        input.setAttribute('value', '0.0');
        input.setAttribute('required', 'true');
    }

}


const daysWeekEnum = {
    'Monday': 1,
    'Tuesday': 2, 
    'Wednesday': 4, 
    'Thursday': 8, 
    'Friday': 16, 
    'Saturday': 32, 
    'Sunday': 64
};