
// redirect to an end point post.
function redirectPost(url, args) {
    const form = document.createElement('form');
    form.setAttribute('method', 'POST');
    form.setAttribute('action', url);

    for (let key in args) {
        let value = args[key]
        input = form.appendChild(document.createElement('input'))
        input.type = 'hidden';
        input.name = key;
        input.value = value;
    }

    document.body.appendChild(form);
    form.submit();
}