package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"sync"
	"time"
)

// Crie um programa que recebe um número inteiro n como argumento e cria n goroutines.
// Cada uma dessas goroutines deve dormir por um tempo aleatório de no máximo 5
// segundos. A main-goroutine deve esperar todas as goroutines filhas terminarem de
// executar para em seguida escrever na saída padrão o valor de n.

func worker(id int, wg *sync.WaitGroup) {
	defer wg.Done()

	// Gere um número aleatório entre 0 e 5 segundos
	rand.Seed(time.Now().UnixNano())
	sleepTime := time.Duration(rand.Intn(5)) * time.Second

	fmt.Printf("Goroutine %d vai dormir por %s\n", id, sleepTime)
	time.Sleep(sleepTime)
	fmt.Printf("Goroutine %d acordou\n", id)
}

func main() {
	if len((os.Args)) != 2 {
		fmt.Println("Uso: go run programa.go <n>")
		return
	}

	n, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("Erro ao analisar o número:", err)
		return
	}

	var wg sync.WaitGroup

	for i := 1; i <= n; i++ {
		wg.Add(1)
		go worker(i, &wg)
	}

	wg.Wait()

	fmt.Printf("Todas as %d goroutines terminaram\n", n)
}
