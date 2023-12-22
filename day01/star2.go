package main

import "fmt"
import "strings"
import "strconv"
import "unicode"
import "bufio"
import "os"

func main() {
	file, err := os.Open("star1.txt")
	if err != nil {
		fmt.Println("Error opening file")
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	sum := 0

	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(line)
		line = strings.Replace(line, "one", "one1one", -1)
		line = strings.Replace(line, "two", "two2two", -1)
		line = strings.Replace(line, "three", "three3three", -1)
		line = strings.Replace(line, "four", "four4four", -1)
		line = strings.Replace(line, "five", "five5five", -1)
		line = strings.Replace(line, "six", "six6six", -1)
		line = strings.Replace(line, "seven", "seven7seven", -1)
		line = strings.Replace(line, "eight", "eight8eight", -1)
		line = strings.Replace(line, "nine", "nine9nine", -1)
		fmt.Println(line)
		first, last := find_digits(line)
		first_converted, err := strconv.Atoi(string(first))
		last_converted, err := strconv.Atoi(string(last))
		fmt.Println(first_converted, last_converted)
		if err != nil {
			fmt.Println(err)
		}
		sum = sum + first_converted*10 + last_converted
	}
	fmt.Println(sum)
}

func find_digits(input string) (rune, rune) {
	var first, last rune
	for _, v := range input {
		if unicode.IsDigit(v) {
			first = v
			break
		}
	}

	for i := len(input) - 1; i >= 0; i-- {
		current_rune := rune(input[i])
		if unicode.IsDigit(current_rune) {
			last = current_rune
			break
		}
	}

	return first, last
}
