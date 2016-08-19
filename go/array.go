package main

import "fmt"

func modify(array [10] int) {
    for i:=0; i < len(array); i++ {
        array[i] = i
        fmt.Printf("array %d = %d\n", i, array[i])
    }    
}

func main() {
    array := [10] int {0,0,0,0,0,0,0,0,0,0}
    modify(array)
    for i:=0; i < len(array); i++ {
        fmt.Printf("array %d = %d\n", i, array[i])
    }    
}
