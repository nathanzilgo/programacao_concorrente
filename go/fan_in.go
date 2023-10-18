package main

import (
	"fmt"
	"time"
)

const maxCapacity = 10

func request_stream() chan string {
	ch := make(chan string)
	go func() {
		for i := 0; i < maxCapacity; i++ {
			ch <- fmt.Sprintf("Request #%d", i)
			time.Sleep(time.Second) // Simulando a produção lenta de dados
		}
		close(ch)
	} ()
	return ch
}

func ingest (in chan string) {
	for item := range in {
		fmt.Println(item)
	}
}

func main() {
	ch1 := request_stream()
	ch2 := request_stream()
	ingestCh := make(chan string)

	go ingest(ingestCh)

	for {
		select {
			case item, ok := <- ch1:
				if ok {
					ingestCh <- item
				} else {
					ch1 = nil
				}
			case item, ok := <- ch2:
				if ok {
					ingestCh <- item
				} else {
					ch2 = nil
				}
		}

		if ch1 == nil && ch2 == nil {
			close(ingestCh)
			break
		}
	}
}