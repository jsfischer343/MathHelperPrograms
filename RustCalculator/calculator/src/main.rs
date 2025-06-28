#![allow(non_snake_case)]

use std::env;

fn calcAdd(x: i32, y: i32) -> i32
{
    return x+y;
}

fn calcSub(x: i32, y: i32) -> i32
{
    return x-y;
}

fn calcMul(x: i32, y: i32) -> i32
{
    return x*y;
}

fn calcDiv(x: i32, y: i32) -> i32
{
    return x/y;
}

fn calcMod(x: i32, y: i32) -> i32
{
    return x%y;
}

fn calcPow(x: i32, y: u32) -> i32
{
    return x.pow(y);
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len()!=4
    {
        println!("Invalid number of argumnets\nUsage: ./calculator <number> <operation> <number>\nOperations: +,-,*,/,%,^");
    }
    else
    {
        let number1 = args[1].parse::<i32>().unwrap();
        let number2 = args[3].parse::<i32>().unwrap();
        let result = match args[2].as_ref()
        {
            "+"=>calcAdd(number1,number2),
            "-"=>calcSub(number1,number2),
            "*"=>calcMul(number1,number2),
            "/"=>calcDiv(number1,number2),
            "%"=>calcMod(number1,number2),
            "^"=>calcPow(number1,number2 as u32),
            _=>-1
        };
        println!("{}",result);
    }
}
