package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

func worker(id int, doneCh chan struct{}) {
	rand.Seed(time.Now().UnixNano())
	sleepTime := time.Duration(rand.Intn(5)) * time.Second

	fmt.Printf("Goroutine %d vai dormir por %s\n", id, sleepTime)
	time.Sleep(sleepTime)
	fmt.Printf("Goroutine %d acordou\n", id)

	doneCh <- struct{}{}
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Uso: go run programa.go <n>")
		return
	}

	n, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("Erro ao analisar o número:", err)
		return
	}

	doneCh := make(chan struct{})

	for i := 1; i <= n; i++ {
		go worker(i, doneCh)
	}

	// Aguarda o sinal de todas as goroutines terminarem
	for i := 0; i < n; i++ {
		<- doneCh
	}

	fmt.Printf("Todas as %d goroutines terminaram\n", n)
	close(doneCh)
}