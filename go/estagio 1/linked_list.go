package main
import "fmt"

type node struct {
	data int
	next *node
}

type linkedList struct {
	head *node
	length int
}

func (l linkedList) print() {
	tmp := l.head
	for l.length != 0 {
		fmt.Printf("%d ", tmp.data)
		tmp = tmp.next
		l.length--
	}
	fmt.Println()
}

func (l *linkedList) prepend(n *node) {
	second := l.head
	l.head = n
	l.head.next = second
	l.length++
}

func main() {
	myList := linkedList{}
	node1 := &node{data: 1}
	node2 := &node{data: 2}
	node3 := &node{data: 3}
	myList.prepend(node1)
	myList.prepend(node2)
	myList.prepend(node3)
	myList.print()
}