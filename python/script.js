function start() {
    var takeNumber = parseInt(prompt('Enter your Number : ')); // Convert input to an integer
    
    if (takeNumber % 2 === 0) {
        console.log("even");
    } else {
        console.log("odd");
    }
}

start();
