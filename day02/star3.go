package main

import "fmt"
// import "strings"
import "strconv"
// import "unicode"
import "bufio"
import "os"

func main() {
	file, err := os.Open("star3.txt")
	if err != nil {
		fmt.Println("Error opening file")
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	sum := 0

	for scanner.Scan() {
		line := scanner.Text()

		for i := len(line) - 1; i >= 0; i-- {
			converted, err := strconv.Atoi(string(line[i]))
			if err != nil {
				fmt.Println(err)
			}
			fmt.Println(converted)
		}

	// 	first_converted, err := strconv.Atoi(string(first))
	// 	last_converted, err := strconv.Atoi(string(last))
	// 	fmt.Println(first_converted, last_converted)
	// 	if err != nil {
	// 		fmt.Println(err)
	// 	}
	// 	sum = sum + first_converted*10 + last_converted
	}
	fmt.Println(sum)
}
		// if unicode.IsDigit(v) {
		// 	first = v
		// 	break
		// }

