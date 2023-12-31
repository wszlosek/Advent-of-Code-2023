package main

import (
	"adventOfCode/utils"
	"strings"
	"unicode"
)

func getNumbersMap() map[string]int {
	return map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}
}

func getFirstNumber(line string) string {
	for _, s := range line {
		if unicode.IsDigit(s) {
			return string(s)
		}
	}

	return ""
}

func getFirstNumberWithWords(line string) string {
	numbers := getNumbersMap()

	for i, s := range line {
		if unicode.IsDigit(s) {
			return string(s)
		}

		for _, key := range utils.GetKeys(numbers) {
			if strings.Contains(line[0:i+1], key) {
				value, _ := numbers[key]
				return utils.ToString(value)
			}
		}
	}

	return ""
}

func getLastNumber(line string) string {
	character := []rune(line)

	for i := len(character) - 1; i >= 0; i-- {
		if unicode.IsDigit(character[i]) {
			return string(character[i])
		}
	}

	return ""
}

func getLastNumberWithWords(line string) string {
	numbers := getNumbersMap()
	character := []rune(line)

	for i := len(character) - 1; i >= 0; i-- {
		if unicode.IsDigit(character[i]) {
			return string(character[i])
		}

		for _, key := range utils.GetKeys(numbers) {
			if strings.Contains(line[i:], key) {
				value, _ := numbers[key]
				return utils.ToString(value)
			}
		}
	}

	return ""
}

func sumNumbers(lines []string) int {
	var numbers []string
	for _, line := range lines {
		a := getFirstNumber(line)
		b := getLastNumber(line)
		numbers = append(numbers, a+b)
	}

	result := 0
	for _, number := range numbers {
		i, _ := utils.ToInt(number)
		result += i
	}

	return result
}

func sumNumbersWithWords(lines []string) int {
	var numbers []string
	for _, line := range lines {
		a := getFirstNumberWithWords(line)
		b := getLastNumberWithWords(line)
		numbers = append(numbers, a+b)
	}

	result := 0
	for _, number := range numbers {
		i, _ := utils.ToInt(number)
		result += i
	}

	return result
}

func main() {
	lines := utils.ReadLines("input/day01.txt")
	println(sumNumbers(lines))
	println(sumNumbersWithWords(lines))
}
