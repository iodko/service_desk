let instances;
let organizationInputs;
let organizationInput;

document.addEventListener('DOMContentLoaded', function () {
        async function getOrganization(search = '') {
            console.log(3)
            const url = '/api/v1/organizations/' + '?search=' + search
            const response = await fetch(url, {
                method: 'GET',
                mode: 'cors',
                cache: 'no-cache',
                headers: {
                    'Content-Type': 'application/json'
                },
            })
            return await response.json();
        }

        console.log(1)
        // init
        organizationInputs = document.querySelectorAll('.autocomplete');
        organizationInput = organizationInputs[0]
        console.log(2)
        instances = M.Autocomplete.init(organizationInputs, {});
        // on actions

        organizationInput.oninput = event => {
            console.log(2)
            getOrganization(event.currentTarget.value).then(data => {
                let obj = {}
                for (let el of data) {
                    obj[el.name] = el.photo
                }
                instances[0].updateData(obj)
            })
        }
    }
);


