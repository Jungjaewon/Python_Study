package main

func main() {

	// Pointer Example
	println("Pointer Example")
	var integer int = 3
	var p = &integer
	var str string = "Example"
	var p_str = &str
	var f float64 = 3.1452
	var p_f = &f
	println(*p)
	println(*p_str)
	println(*p_f)

	println("If Statement")
	// If statement
	if true { //  if 1 {} does not work
		println("1 is always true")
	}

	var base int = 1
	// else if , else must be located after }
	if base == 1 {
		println("One")
	} else if base == 2 {
		println("Two")
	} else {
		println("Three")
	}

	if val := base * 2; val < 5 {
		println("val is less than 5")
	}
	// val scope is only if statement // like that for(int i; i < size ;++i)
}
