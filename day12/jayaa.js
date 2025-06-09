// for in loop
let a={name:"Baby",marks:98};
for(let i in a)
    console.log(a[i]);
// for of loop
let nums = [10, 20, 30];
for (let num of nums) {
  console.log(num);
}

let colors = ["red", "green", "blue"];
console.log(colors);
console.log(colors[0]);
colors[1] = "yellow";
console.log(colors);
console.log(colors.length);
for (let j=0;j<colors.length;j++){
    console.log(colors[j])
}



// Array
let Arr=["BABY","JAYA","KEERTHI","MOUNI"];
Arr[0]="Sony"
console.log(Arr);
console.log(Arr[3]);
console.log(Arr.length);
for(let i=0;i<Arr.length;i++){
    console.log(Arr[i])
}

//Array Methods
Arr.push(23)   // push an element to the last of the present array
console.log(Arr);
Arr.pop()      // pop the last element in the given array
console.log(Arr);
Arr.shift()    //remove the 1st index to the given array
console.log(Arr);
Arr.unshift("Namina")   // Add an  element in 1st index to the given array
console.log(Arr);
