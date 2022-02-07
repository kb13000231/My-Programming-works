package main

import "fmt"

func main() {
	fmt.Println("Welcome to the awesome quiz game!!")

	fmt.Printf("Please enter your name: ")
	var name string
	fmt.Scan(&name)
	fmt.Printf("Hello, %v, Let's play the quiz game!", name)

	fmt.Printf("Please enter your age: ")
	var age uint
	fmt.Scan(&age)

	if age >= 10 {
		fmt.Println("Yay! you can play this game.")
	} else {
		fmt.Println("You cannot play this game. Only for Age 10+")
		return
	}

}
