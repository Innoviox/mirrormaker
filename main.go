package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	f, err := os.Open("test_sword.txt")
	if err != nil {
		panic(err)
	}

	defer f.Close()

	// https://stackoverflow.com/questions/8757389/reading-a-file-line-by-line-in-go/16615559#16615559
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
