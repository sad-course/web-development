const cpfInputField = document.querySelector("#cpfInput")
const phoneInputField = document.querySelector("#phoneInput")

cpfInputField.addEventListener("keypress", (event) => {
    let cpfInputValue = event.target.value; 

    if (cpfInputValue.length == 3 || cpfInputValue.length == 7){
        cpfInputValue += ".";
    }else{
        if(cpfInputValue.length == 11){
            cpfInputValue += "-";
        }
    }
    cpfInputField.value = cpfInputValue;
})

phoneInputField.addEventListener("keypress", (event) => {
    let phoneInputValue = event.target.value;

    if (phoneInputValue.length == 0){
        phoneInputValue += "("
    }else{
        if (phoneInputValue.length == 3){
            phoneInputValue += ")"
        }
        if(phoneInputValue.length == 9){
            phoneInputValue += "-"
        }
    }
    phoneInputField.value = phoneInputValue
})

function validateInputs(){
    
}