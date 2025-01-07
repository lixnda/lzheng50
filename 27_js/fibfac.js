//Linda Zheng
//SoftDev pd4
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:
function factorial(num) {
    if (num == 1) {
        return num;
    } else {
        return num * factorial(num - 1);
    }
}
//<your team's fact(n) implementation>

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
factorial(1)
factorial(2)
factorial(3)
factorial(4)
factorial(5)

//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>
function fibonacci(num) {
    if (num < 2) {
        return num;
    } else {
        return fibonacci(num - 2) + fibonacci(num - 1);
    }
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fibonacci(1)
fibonacci(2)
fibonacci(3)
fibonacci(4)
fibonacci(5)

//=================================================================