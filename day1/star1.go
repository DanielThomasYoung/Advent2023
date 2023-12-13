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
		line = strings.Replace(line, "one", "1", -1)
		line = strings.Replace(line, "two", "2", -1)
		line = strings.Replace(line, "three", "3", -1)
		line = strings.Replace(line, "four", "4", -1)
		line = strings.Replace(line, "five", "5", -1)
		line = strings.Replace(line, "six", "6", -1)
		line = strings.Replace(line, "seven", "7", -1)
		line = strings.Replace(line, "eight", "8", -1)
		line = strings.Replace(line, "nine", "9", -1)
		fmt.Println(line)
		first, last := find_digits(line)
		first_converted, err := strconv.Atoi(string(first))
		last_converted, err := strconv.Atoi(string(last))
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
