/*

    Abaixo de 18,5 Baixo Peso
    Entre 18,6 e 24,9 Peso normal
    Entre 25 e 29,9 Sobrepeso
    Entre 30 e 34,9 Obesidade grau I
    Entre 35 e 39,9 Obesidade grau I
    Acima de 40 Obesidade grau III
*/

const buttonImc = document.querySelector("#btnCalc")
    buttonImc.addEventListener("click", (event) => {
        const userHeightInput = document.querySelector("#inputHeight").value;
        const userWeightInput = document.querySelector("#inputWeight").value;
        
        if (userHeightInput === "" || userWeightInput === ""){
            alert("É necessário preencher os campos!")
            return 
        }
        const imc = userWeightInput / (Math.pow(userHeightInput,2));

        const formElement = document.querySelector(".calculatorForm")

        let result = "";
        if (imc < 18.5){
            result = "Abaixo do peso"
        }
        if ((imc >= 18.6) && (imc <= 24.9)){
            result = "Peso normal"
        }
        if((imc >= 25.0) && (imc <= 29.9)){
            result = "Sobrepeso"
        }
        if ((imc >= 30) && (imc <= 34.9)){
            result = "Obesidade Grau I"
        }
        if ((imc >= 35) && (imc <= 39.9)){
            result = "Obesidade Grau II"
        }
        if (imc >= 40){
            result = "Obesidade Grau III"
        }


        if (!document.querySelector("#imcResult")){
            let resultSpan = document.createElement("span")
            resultSpan.id = "imcResult"
            formElement.appendChild(resultSpan)
        }
        document.querySelector("#imcResult").innerText = result
        

})