package main

// Ref 1 : http://golang.site/go/article/19-Go-%EC%97%90%EB%9F%AC%EC%B2%98%EB%A6%AC
import (
	"log"
	"os"
)

// This example is for error handling
//
func main() {
	f, err := os.Open("C:\\temp\\1.txt") //  func Open(name string) (file *File, err error)
	if err != nil {
		log.Fatal(err.Error()) // print message and call exit(1)
	}
	println(f.Name())
}
