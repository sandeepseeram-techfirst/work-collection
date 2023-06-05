package main

import "fmt"

func main() {
    m := map[string]int{}
    m2 := map[string]int{
        "a": 1,
        "b": 2,
        "c": 3,
    }
    m3 := make(map[string]int)

    fmt.Println(m, m2, m3)
    m["hello"] = 20
    fmt.Println(m["hello"])
    fmt.Println(len(m), len(m2), len(m3))
    //more
}
