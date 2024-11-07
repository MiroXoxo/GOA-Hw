// 11. **Find the Maximum**  
// Create a function `find_max` that accepts three numbers and returns the largest one using comparison operators and if-else statements.
document.getElementById("submit-max").onclick=function(){
    let a=document.getElementById("num1").value;
    let b=document.getElementById("num2").value;
    let c=document.getElementById("num3").value;
    let max;
    if(a>b && a>c){
        max=a;
    }else if(b>a&&b>c){
        max=b;
    }else if(c>a&&c>b){
        max=c;
    }
    if(a===b && a>c){
        max=a;
    }else if(b===c && b>a){
        max=b;
    }else if(a===c && a>b){
        max=a;
    }else if(a===c && c===b){
        max=a;
    }
    document.getElementById("display-max").textContent=max;
}
// 12. **Pass or Fail**  
// Write a function `pass_or_fail` that accepts a student's score and returns "Pass" if the score is 50 or above, and "Fail" otherwise.
document.getElementById("submit-score").onclick=function(){
    let score;
    let passFail;
    let color;
    score=Number(document.getElementById("score").value);
    if(score<50){
        passFail="You Failled !"
        color="red"
    }else{
        passFail="You Passed !"
        color="green"
    }
    document.getElementById("pass-fail").textContent=passFail;
    document.getElementById("pass-fail").style.color=color;
}
