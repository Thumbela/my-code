package main

import "fmt"

func main(){
	fmt.Println('Enter your name : ')
	var name string
	fmt.Scanln(&name)
	fmt.Printf("Hi, %s! I am the coder",name)
}