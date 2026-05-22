
// redirect to an end point post.
function redirectPost(url, ...args) {
    const form = document.createElement('form');
    form.setAttribute('method', 'POST');
    form.setAttribute('action', url);

    args.forEach(arg => {
        input = form.appendChild(document.createElement('input'))
        input.type = 'hidden';
        input.name = arg[0];
        input.value = arg[1];
    });

    document.body.appendChild(form);
    form.submit();
}