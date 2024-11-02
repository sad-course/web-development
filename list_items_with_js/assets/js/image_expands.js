const imageToExpand = document.querySelector("#firstImage")
const imageToExpand2  = document.querySelector("#secondImage")

const sectionImageExpanded = document.querySelector(".section-image")
const imageDiv = document.querySelector(".image-expanded")
const imageExpanded = document.querySelector(".image-expanded>img")

let isExpanded = false;

imageToExpand.addEventListener("click", (event) => {    
    srcImage = imageToExpand.getAttribute("src");
    sectionImageExpanded.style.display = "flex";
    imageExpanded.setAttribute("src", srcImage);
    isExpanded = true;
})

imageToExpand2.addEventListener("click", (event) => {    
    srcImage = imageToExpand2.getAttribute("src");
    sectionImageExpanded.style.display = "flex";
    imageExpanded.setAttribute("src",srcImage);
    isExpanded = true;
})

imageDiv.addEventListener("click", (event) => {
    if (isExpanded){
        sectionImageExpanded.style.display = "none";
        isExpanded = false;
    }
})

sectionImageExpanded.addEventListener("click", (event) => {
    if (isExpanded){
        sectionImageExpanded.style.display = "none";
        isExpanded = false;
    }
})