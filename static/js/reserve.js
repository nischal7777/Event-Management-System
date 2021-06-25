const submit = document.getElementById("submit-btn");

const fetchForm = () => {
    let name = document.getElementById("form-name").value;
    let email = document.getElementById("form-email").value;
    let phone = document.getElementById("form-phone").value;
    let date = document.getElementById("form-date").value;
    let formData = [name, email, phone, date];
    return formData;
}

const postData = () => {
    const formData = fetchForm();
    axios.post("http://localhost:8000/api/book/", {
        "name": formData[0],
        "email": formData[1],
        "phone": formData[2],
        "date": formData[3]
    })
    .then(response => {
        console.log(response.data);
        const message = "<p style=\"color:green;\">Successfully Reserved</p>";
        const modalBody = document.getElementById("success-modal-body");
        modalBody.innerHTML = message;
        const modal = document.getElementById("trigger-modal");
        modal.click();
        document.getElementById("form-name").value = "";
        document.getElementById("form-email").value = "";
        document.getElementById("form-phone").value = "";
        document.getElementById("form-date").value = "";
    })
    .catch(error => {
        if (error.response) {
            console.error(error.response.status);
            console.error(error.response.data);
        }
        const message = "<p style=\"color:red;\">Venue Already Reserved. Try Another Date.</p>";
        const modalBody = document.getElementById("success-modal-body");
        modalBody.innerHTML = message;
        const modal = document.getElementById("trigger-modal");
        modal.click();
    })
}

const formOnSubmit = (bid) => {
    bid.addEventListener("click", (e) => {
        e.preventDefault();
        console.log(fetchForm());
        postData();
    });
}

formOnSubmit(submit);
