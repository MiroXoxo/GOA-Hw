// 1.Multiply Two Numbers
// Write a function multiply() that prompts the user to input two numbers and returns their product.
let num1;
let num2;
let multi;
document.getElementById("multi").onclick=function(){
    num1=document.getElementById("num1").value;
    num2=document.getElementById("num2").value;
    multi=num1*num2;
    document.getElementById("result-multi").textContent=`${num1} * ${num2} = ${multi}`;
}
// 2.Subtract Two Numbers
// Write a function subtract() that prompts the user for two numbers and returns the difference.
let numb1;
let numb2;
let sub;
document.getElementById("sub").onclick=function(){
    numb1=document.getElementById("numb1").value;
    numb2=document.getElementById("numb2").value;
    sub=numb1-numb2;
    document.getElementById("result-sub").textContent=`${numb1} - ${numb2} = ${sub}`;
}
// 3.Divide Two Numbers
// Write a function divide() that prompts the user for two numbers and returns their quotient.
let numbe1;
let numbe2;
let div;
document.getElementById("div").onclick=function(){
    numbe1=document.getElementById("numbe1").value;
    numbe2=document.getElementById("numbe2").value;
    div=numbe1/numbe2;
    document.getElementById("result-div").textContent=`${numbe1} / ${numbe2} = ${div}`;
}
// 4.Return a Full Name
// Write a function fullName() that prompts the user to input their first name and last name, and returns the full name as a single string.
let firstName;
let secondName;
let fullName;
document.getElementById("connect").onclick=function(){
    firstName=document.getElementById("first-name").value;
    secondName=document.getElementById("second-name").value;
    document.getElementById("result-fullname").textContent=`Full Name:\n${firstName}  ${secondName}`;
}
// 5.Convert Minutes to Seconds
// Write a function minutesToSeconds() that prompts the user for a number of minutes and returns the equivalent in seconds.
let min;
let sec;
document.getElementById("convert").onclick=function(){
    min=document.getElementById("minutes").value;
    sec=min*60;
    document.getElementById("seconds").textContent=`${min} Minutes = ${sec} Seconds`
}
// 6.Calculate the Area of a Rectangle
// Write a function rectangleArea() that prompts the user to input the length and width of a rectangle and returns the area.
let len;
let wid;
let area;
document.getElementById("area").onclick=function(){
    len=document.getElementById("length").value;
    wid=document.getElementById("width").value;
    area=len*wid;
    document.getElementById("result-area").textContent=`The Area Of The Rectangle Is ${area}`;
}
// 7.Concatenate Two Strings
// Write a function concatenateStrings() that prompts the user for two strings and returns them concatenated together.
let firstString;
let secondString;
let ConnectedString;
document.getElementById("connect-strings").onclick=function(){
    firstString=document.getElementById("first-string").value;
    secondString=document.getElementById("second-string").value;
    document.getElementById("result-connected-string").textContent=`Connected:\n${firstString}${secondString}`;
}
//8.Exponentiation
//Write a function power() that prompts the user for a base number and an exponent, and returns the result of raising the base to the power of the exponent.
let x;
let a;
let resultPower;
document.getElementById("power-result").onclick=function(){
    x=document.getElementById("x").value;
    a=document.getElementById("a").value;
    resultPower=a**x;
    document.getElementById("power").textContent=x;
    document.getElementById("base").textContent=`${a} = ${resultPower}`;
}
//9.Calculate Circle Circumference
//Write a function circumference() that prompts the user to input a circle's radius and returns the circumference.
let r;
let resultC;
document.getElementById("c").onclick=function(){
    r=document.getElementById("radius").value;
    resultC=2*3.14*r;
    document.getElementById("result-c").textContent=`C = ${resultC}`;
}
//10.Return the Next Number
//Write a function nextNumber() that prompts the user for a number and returns the next number (the input number plus one).
let number;
let nextNumber;
document.getElementById("next").onclick=function(){
    number=document.getElementById("number").value;
    nextNumber=number*1+1;
    document.getElementById("next-number").textContent=`Next Number Is ${nextNumber}`;
}