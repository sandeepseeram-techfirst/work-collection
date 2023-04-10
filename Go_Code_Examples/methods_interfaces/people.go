package main

import (
    "fmt"
    "time"
)

type Employee struct {
    ID        int
    FirstName string
    LastName  string
    DateHired time.Time
}

func main() {
    e1 := Employee{
        ID:        1,
        FirstName: "Bob",
        LastName:  "Bobson",
        DateHired: time.Date(2020, time.January, 10, 0, 0, 0, 0, time.UTC),
    }
    e2 := Employee{
        ID:        2,
        FirstName: "Mary",
        LastName:  "Maryson",
        DateHired: time.Date(2007, time.March, 30, 0, 0, 0, 0, time.UTC),
    }
    fmt.Println(e1.FirstName)
    fmt.Println(e2.DateHired)
    // Bob got married and changed his last name
    e1.LastName = "Bobson-Smith"
    fmt.Println(e1.LastName)
}
