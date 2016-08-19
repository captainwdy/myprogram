package main

import "fmt"
import "time"

func main() {
    ch := make(chan int, 1)
    for {
        select {
            case ch <- 0:
            case ch <- 1:
        }
        i := <- ch
        fmt.Println("i=", i)
        time.Sleep(1000000000)
    }
}
