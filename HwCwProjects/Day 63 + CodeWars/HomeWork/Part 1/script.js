//1. **Greeting Function**  
//Create a function `greet` that accepts a name as a parameter and greets the person. If no name is provided, the default name should be "Guest".
function greet(){
    let name;
    name=document.getElementById("login-name").value;
    document.getElementById("greeting").textContent=`Hello ${name}`;
}
document.getElementById("log").onclick=greet;
//2. **Addition with Default Parameters**  
//Write a function `add_numbers` that takes two numbers and returns their sum. The second number should have a default value of 0.
function add_numbers(){
    let result;
    let num2=0
    let num1;
    num1=document.getElementById("num1").value;
    num2=document.getElementById("num2").value;
    result=Number(num1)+Number(num2);
    document.getElementById("added-number").textContent=`${result}`;
}
document.getElementById("add-numbers").onclick=add_numbers;
//3. **Rectangle Area Calculator**  
// Create a function `calculate_area` to find the area of a rectangle. It should take two parameters: length and width. If the width is not provided, use a default value of 1.
let len;
let wid;
let area;
document.getElementById("area").onclick=function(){
    len=document.getElementById("length").value;
    wid=document.getElementById("width").value;
    area=len*wid;
    document.getElementById("result-area").textContent=`The Area Of The Rectangle Is ${area}`;
}
//4. **Temperature Conversion**  
//Write a function `convert_temperature` to convert temperatures between Celsius and Fahrenheit. It should have two parameters: temperature and scale (either "C" for Celsius or "F" for Fahrenheit), with "C" as the default scale.
let toggleC=true;
let toggleDisplay=document.getElementById("toggle-display1");
let toggleDisplay1=document.getElementById("toggle-display2");
let inputField=document.getElementById("input-temp");
let resultDisplay=document.getElementById("result-temp");
toggleDisplay.textContent="C To F";
toggleDisplay1.textContent="Input Celsius";

document.getElementById("toggle-scale").onclick=function(){
    toggleC= !toggleC;
    if(toggleC){
        toggleDisplay.textContent="C To F";
        toggleDisplay1.textContent="Input Celsius";
    }
    else{
        toggleDisplay.textContent="F To C";
        toggleDisplay1.textContent="Input Fahrenheit"
    }
    inputField.value='';
};
document.getElementById("convert").onclick=function(){
    let input = Number(inputField.value);
    let resultTemp;

    if(toggleC){
        resultTemp=input*1.8+32;
    }
    else{
        resultTemp=(input-32)*(5/9);
    }
    resultDisplay.textContent=`${resultTemp}°`
}