package main

import "fmt"

func main() {
    s1 := "This is an interpreted string literal.\n\tIt must be written on a single line.\n\tEscape sequences are evaluated."
    fmt.Println(s1)

    s2 := `This is a raw string literal.
    It can be written across multiple lines.
    Escape sequences like \n are not evaluated.`
    fmt.Println(s2)
}