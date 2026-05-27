


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
    exerciceToDoContainer.classList.add('exercice-to-do-container', 'card', 'card-body', 'mt-2');
    exerciceToDoContainer.setAttribute('index-exo', indexExo);


    // fill block inputs exercice-to-do.
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
                    value: e.innerText.toLowerCase(),
                    id: e.getAttribute('value')
                };
            }).find(e => e.value == valueInput);
            
            if (
                (valueInput === "" && inputEnumExo.hasAttribute('required'))  // input empty (when required).
                ||
                enumMatch === undefined  // value not in enum range.
            ) {
                inputEnumExo.classList.add('is-invalid');
                inputEnumExo.classList.remove('is-valid');
                inputEnumExo.removeAttribute('type-exo-id');
            } else {  // valide.
                inputEnumExo.classList.add('is-valid');
                inputEnumExo.classList.remove('is-invalid');
                inputEnumExo.setAttribute('type-exo-id', enumMatch.id);
            }

        });
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
    }

    // reps.
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
    }

}

