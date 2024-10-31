const itemInput = document.querySelector("#itemTextInput")
const btnAddItem = document.querySelector("#addItemBtn")
const shopList = document.querySelector("#shopItemsList")

itemInput.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        event.preventDefault();
        btnAddItem.click();
    }
})

btnAddItem.addEventListener("click", (event) =>{
    let itemValue = itemInput.value;
    if (itemValue === ""){
        alert("O campo deve ser preenchido");
        return
    }

    let newItem = document.createElement("li");
    newItem.innerText = itemValue;
    shopList.appendChild(newItem);
})

