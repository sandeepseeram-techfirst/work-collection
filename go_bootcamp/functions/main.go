package main

import (
    "fmt"
    //more1
)

func main() {
    if len(os.Args) != 3 {
        fmt.Println("Two integer parameters expected")
        os.Exit(1)
    }
    a, err := strconv.Atoi(os.Args[1])
    if err != nil {
        fmt.Println("invalid first argument:", err)
        os.Exit(1)
    }
    b, err := strconv.Atoi(os.Args[2])
    if err != nil {
        fmt.Println("invalid second argument:", err)
        os.Exit(1)
    }
    add := adder
    sub := subtractor
    mul := multiplier
    div := divider
    c, err := add(a, b)
    if err != nil {
        fmt.Println("adding failed:", err)
    } else {
        fmt.Println(c)
    }
    d, err := sub(a, b)
    if err != nil {
        fmt.Println("subtracting failed:", err)
    } else {
        fmt.Println(d)
    }
    e, err := mul(a, b)
    if err != nil {
        fmt.Println("multiplying failed:", err)
    } else {
        fmt.Println(e)
    }
    f, err := div(a, b)
    if err != nil {
        fmt.Println("dividing failed:", err)
    } else {
        fmt.Println(f)
    }
}
