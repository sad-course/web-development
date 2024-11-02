const openMenuButton = document.querySelector("#openMenuBtn")
const navBarSection = document.querySelector(".navbar")
const navBarItems = document.querySelector(".navbar-items")
const menuIcon = document.querySelector("#openMenuBtn>img")

openMenuButton.addEventListener("click", (event) => {
    let displayToSet = "none";
    let navBarWidth = "40px";
    if (navBarItems.style.display == "none"){
        displayToSet = "flex";
        navBarWidth = "300px";
        
        menuIcon.style.transform = "rotate(90deg)";
        menuIcon.style.transition = "transform 0.7s ease"
    }else{
        menuIcon.style.transform = "rotate(0deg)";
        menuIcon.style.transition = "transform 0.7s ease"
    }
    navBarItems.style.display = displayToSet;
    navBarSection.style.width = navBarWidth;
    navBarSection.style.transition = "width 1s ease"
})

