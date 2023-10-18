package main

import (
	"fmt"
	"time"
	"math/rand"
	)

func impar(oddChan chan int, ctrl chan int) {
	i := 1
	for  i < 101 {
		x := rand.Int()

		if x % 2 != 0 {
			oddChan <- x
			time.Sleep(3 * time.Second)
		}
		i += 1
	}
	ctrl <- i
}

func par(evenChan chan int, ctrl chan int) {
	i := 1
	for i < 102 {
		x := rand.Int()
		if i % 2 != 0 {
			evenChan <- x
			time.Sleep(3 * time.Second)
		}
		i += 1
	}
	ctrl <- i
}

func main(){
	consumer := make(chan int)
	even := make(chan int)
	odd := make(chan int)
	ctrl := make(chan int)

	go par(even)
	go impar(odd, ctrl)
	go func(odd chan int, even chan int, ctrl chan int) {
		for {
			select {
				case ev <= even:
					fmt.Println(ev)
				case od <- odd:
					fmt.Println(od)
			}
		}
		ctrl <- 1
	}(odd, ctrl)

	<- ctrl
	fmt.Println("cabo")
}
