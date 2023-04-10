package main

import (
    "fmt"
    //more1
)

func main() {
    a := 20
    b := 10
    c := adder(a, b)
    fmt.Println(c)
    d := subtractor(a, b)
    fmt.Println(d)
    e := multiplier(a, b)
    fmt.Println(e)
    f := divider(a, b)
    fmt.Println(f)
}

func adder(a, b int) int {
    return a + b
}

func subtractor(a, b int) int {
    return a - b
}

func multiplier(a, b int) int {
    return a * b
}

func divider(a, b int) int {
    return a / b
}
