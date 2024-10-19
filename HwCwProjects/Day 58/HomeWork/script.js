//1. **Create an object**: Make an object called `car` with properties like `brand`, `model`, and `year`.
let car={
    brand:"Opel",
    model:"Astra",
    year:2000,
}
//2. **Access object properties**: Using the `car` object, access the `brand` and `year` properties and print them.
console.log(car.brand);
console.log(car.model);
console.log(car.year);
//3. **Add a new property**: Add a new property `color` to the `car` object.
car.color = "Red";
//4. **Change a property value**: Update the `year` property of the `car` object to a new value.
car.year=2004;
//5. **Delete a property**: Remove the `model` property from the `car` object.
delete car.model;
//6. **Create a method**: Add a method `startEngine` to the `car` object that prints "Engine started".
car.startEngine=function(){console.log("Engine Started");};
console.log(car.startEngine);
car.startEngine();
//7. **Object inside an object**: Create a new object `owner` inside the `car` object with properties like `name` and `age`.
car.owner={
    name:"Bob",
    age:"54",
}
console.log(car);