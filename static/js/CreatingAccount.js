function ShowLeadForm(element){
    var leadForm = document.getElementById('LeadForm');
    leadForm.style.display = "flex";   
}
function CheckLeadForm(element){
    var form = document.getElementById('LeadForm');
    var error = document.getElementById('error');

    if (form.firstName.value == "" ||
        form.name.value == "" ||
        form.group.value == "" ||
        form.email.value == "" ||
        form.pass.value == "" ||
        form.repass.value == "")
        {
        PrintError("Все поля должны быть заполнены");
        return false;
    }
    else {
        console.log("f ok")
    }

    if (CheckLenght(form.firstName.value, 20, 2))
    {
        PrintError("Ваше имя слишком короткое или слишком длинное");
        return false;
    }
    else {
        console.log("fn ok")
    }

    if (CheckLenght(form.name.value, 20, 2)) {
        PrintError("Ваша фамилия слишком короткая или слишком длинная");
        return false;
    }
    else {
        console.log("n ok")
    }

    if (CheckLenght(form.group.value, 10, 2)) {
        PrintError("Название группы слишком короткое или слишком длинное");
        return false;
    }
    else {
        console.log("g ok")
    }

    if (CheckLenght(form.pass.value, 30, 4)) {
        PrintError("Длинна пароля должна быть от 4 до 30 символов");
        return false;
    }
    else {
        console.log("pl ok")
    }

    if (CheckLenght(form.pass.value != form.repass.value)) {
        PrintError("Пороли не совпадают");
        return false;
    }
    else {
        console.log("pc ok")
    }
    form.id = "form";
}

function CheckLenght(string, Mlenght, mlenght) {
    if (string.length < mlenght || string.length > Mlenght) {
        return true;
    }
    else {
        return false;
    }
}

function PrintError(string) {
    var error = document.getElementById('error');
    error.style.display = "flex";
    error.innerHTML = string;
}
