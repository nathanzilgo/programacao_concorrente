package main


import (
	"fmt"
	"time"
)

const maxCapacity = 10

type Request struct {
	ID int
}

func create_req() Request {
	return Request{ID: time.Now().Nanosecond()}
}

func exec_req(req Request) {
	// Simular o processamento demorado
	time.Sleep(2 * time.Second)
	fmt.Printf("Requisição %d processada\n", req.ID)
}

func main() {
	reqChan := make(chan Request, maxCapacity)
	doneCh := make(chan Request)
	
	go func () {
		for req := range reqChan {
			exec_req(req)
			doneCh <- req
		}
	} ()

	for {
		select {
			case reqChan <- create_req():
				fmt.Printf("Requisição criada\n")
			case req := <- doneCh:
				fmt.Printf("Requisicao %d processada\n", req.ID)
		}
	}
}
