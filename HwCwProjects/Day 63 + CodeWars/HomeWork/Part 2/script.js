// 5. **Shopping List**  
// Create a function `add_to_shopping_list` that accepts an item and a quantity. The quantity should default to 1 if not provided.
let shoppingList = [];
let item;
let quantity;
document.getElementById("shop-submit").onclick=function() {
    item=document.getElementById("item").value;
    quantity=document.getElementById("amount").value || 1;
    shoppingList.push({ item, quantity });
    console.log(`${quantity} x ${item} Added To The Shopping List`);

    document.getElementById("item").value = '';
    document.getElementById("amount").value = 1;
}
// 6. **Power Function**  
// Write a function `power` that calculates the power of a number with a default exponent value of 2 (i.e., square).
let x;
let a;
let resultPower;
document.getElementById("power-result").onclick=function(){
    x=document.getElementById("x").value;
    if(x===""){
        x=2;
    }
    a=document.getElementById("a").value;
    resultPower=a**x;
    document.getElementById("power").textContent=x;
    document.getElementById("base").textContent=`${a} = ${resultPower}`;
}
// 7. **Personalized Message**  
// Create a function `create_message` that generates a personalized message given a name and an optional greeting ("Hello" as default).
function greet(){
    let name;
    let greetOption;
    greetOption=document.getElementById("greet-option").value||"Hello";
    name=document.getElementById("login-name").value;
    document.getElementById("greeting").textContent=`${greetOption} ${name}`;
}
document.getElementById("log").onclick=greet;
// 8. **Calculate Discount**  
// Write a function `apply_discount` that calculates the final price of an item after applying a discount. The discount should be a default of 10%.
let result;
document.getElementById("disc-calculate").onclick=function(){
    let price;
    let discount;
    price=document.getElementById("price").value;
    discount=document.getElementById("precent").value;
    if(discount===""){
        discount=10;
    }
    
    result=Number(price)-(Number(price)*Number(discount)/100);
    document.getElementById("fin-price").textContent=`Discounted Price Is ${result}`;
}
// 9. **Introduction Function**  
// Create a function `introduce` that takes a name, age, and country. If age and country are not provided, they should default to "unknown".
let name;
let age;
let country;
document.getElementById("introduce").onclick=function(){
    name=document.getElementById("name").value;
    age=document.getElementById("age").value;
    if(age===""){
        age="Uknown"
    }
    country=document.getElementById("country").value;
    if(country===""){
        country="Uknown"
    }
    document.getElementById("nac").textContent=`Details\n\nName: ${name}\nAge: ${age}\nCountry: ${country}`;
}
// 10. **Calculate Final Price**  
// Write a function `calculate_price` that takes the price of an item and a sales tax. The sales tax should default to 5%.

document.getElementById("calculate").onclick=function(){
    let result;
    let price;
    let tax;
    price=document.getElementById("price-before").value;
    tax=document.getElementById("tax-precent").value;
    if(tax===""){
        tax=5;
    }
    
    result=Number(price)+(Number(price)*Number(tax)/100);
    document.getElementById("after-tax").textContent=`After Tax Price Is ${result}`;
}