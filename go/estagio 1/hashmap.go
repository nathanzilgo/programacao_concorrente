package main

import "fmt"

const ArraySize = 10

type HashTable struct{
	array [ArraySize]*bucket
}

type bucket struct{
	head *bucketNode
}

type bucketNode struct{
	key string
	next *bucketNode
}

func Init() *HashTable {
	result := &HashTable{}
	for i := range result.array {
		result.array[i] = &bucket{}
	}
	return result
}

func main() {
	map1 := make(map[string]int)
	map1["a"] = 1
	map1["b"] = 2
	map1["c"] = 3
}