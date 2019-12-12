package main

// Ref 1 : http://golang.site/go/article/19-Go-%EC%97%90%EB%9F%AC%EC%B2%98%EB%A6%AC

// custom error return, var example is neened.
// Myerror must be declared on the code.

import "log"

func otherFunc() (int, error) {
	return 1, nil
}

func main() {
	_, err := otherFunc()
	switch err.(type) {
	default: // no error
		println("ok")
	//case MyError:
	//	log.Print("Log my error")
	case error:
		log.Fatal(err.Error())
	}

}
