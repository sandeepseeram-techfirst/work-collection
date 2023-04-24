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

var Employees = map[int]Employee{}
var nextID = 0

func AddEmployee(firstName, lastName string, dateHired time.Time) int {
    nextID++
    Employees[nextID] = Employee{
        ID:        nextID,
        FirstName: firstName,
        LastName:  lastName,
        DateHired: dateHired,
    }
    return nextID
}

func GetEmployee(id int) (Employee, bool) {
    p, ok := Employees[id]
    return p, ok
}

func DMYToTime(day int, month time.Month, year int) time.Time {
    return time.Date(year, month, day, 0, 0, 0, 0, time.UTC)
}

func main() {
    e1ID := AddEmployee("Bob", "Bobson", DMYToTime(10, time.January, 2020))
    e2ID := AddEmployee("Mary", "Maryson", DMYToTime(30, time.March, 2007))
    e1, exists1 := GetEmployee(e1ID)
    e2, exists2 := GetEmployee(e2ID)
    fmt.Println(e1, exists1)
    fmt.Println(e2, exists2)
    e3, exists3 := GetEmployee(2000)
    fmt.Println(e3, exists3)
}
