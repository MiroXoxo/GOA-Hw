// 13. **Sum of Numbers**  
// Write a function `sum_of_numbers` that accepts a list of numbers and returns their sum using a for loop.
let numbers=[]
document.getElementById("input").onclick=function(){
let number;
number=document.getElementById("number").value;
numbers.push(number);
document.getElementById("number").value ="";
}
document.getElementById("get-sum").onclick=function(){
    console.log(numbers)
    let i,len,sum;
    for(i = 0,len=numbers.length,sum=0;i<len;i++){
    sum+=Number(numbers[i]);   
}
   document.getElementById("sum").textContent=sum 
}
document.getElementById("reset").onclick=function(){
    numbers=[];
    document.getElementById("sum").textContent="";
}
// 14. **Count Even Numbers**  
// Create a function `count_evens` that accepts a list of integers and returns the count of even numbers using a for loop.
let numbers1=[];
document.getElementById("input1").onclick=function(){
    let number1;
    number1=document.getElementById("number1").value;
    numbers1.push(Number(number1));
    document.getElementById("number1").value ="";
    }
document.getElementById("get-even").onclick=function(){
    console.log(numbers1)
    let b,len1,even;
    for(b = 0,len1=numbers1.length,even=0;b<len1;b++){
    if(numbers1[b]%2===0){
        even+=1;
    }
}
document.getElementById("even").textContent=`Even Numbers: ${even}`;
}
document.getElementById("reset1").onclick=function(){
    numbers1=[];
    document.getElementById("even").textContent="";
}
