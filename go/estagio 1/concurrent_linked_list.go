package main

import "fmt"

type Node struct {
	key int
	next *Node
}

type LinkedList struct {
	head *Node
	length int
}

func (l *LinkedList) init() {
	l.head = nil
	l.length = 0
}

func (l LinkedList) insert(key int) {
	new := Node{}
	new.key = key
	new.next = l.head
	l.head = &new
}