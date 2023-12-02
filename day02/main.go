package main

import (
	"adventOfCode/utils"
	"strings"
)

func getEmptyMapWithColors() map[string]int {
	return map[string]int{
		"red":   12,
		"green": 13,
		"blue":  14,
	}
}

func maxNumberOfCubes() map[string]int {
	return map[string]int{
		"red":   0,
		"green": 0,
		"blue":  0,
	}
}

func getId(line string) (int, error) {
	return utils.ToInt(strings.Split(strings.Split(line, "Game ")[1], ":")[0])
}

func a(subset string, colors map[string]int) bool {
	keys := utils.GetKeys(colors)
	elements := strings.Split(subset, ",")

	for _, element := range elements {
		for _, key := range keys {
			if strings.Contains(element, key) {
				number := strings.Replace(element, key, "", -1)
				number = strings.Replace(number, " ", "", -1)
				numberInt, _ := utils.ToInt(number)
				colors[key] -= numberInt
				if colors[key] < 0 {
					return false
				}
			}
		}
	}

	return true
}

func b(subset string, cubes map[string]int) int {
	keys := utils.GetKeys(cubes)
	elements := strings.Split(subset, ",")
	result := 1

	for _, element := range elements {
		for _, key := range keys {
			if strings.Contains(element, key) {
				number := strings.Replace(element, key, "", -1)
				number = strings.Replace(number, " ", "", -1)
				s, _ := utils.ToInt(number)
				if cubes[key] < s {
					cubes[key] = s
				}
			}
		}
	}

	for _, key := range keys {
		result *= cubes[key]
	}

	return result
}

func first(lines []string) string {
	var listId []int
	allIdSum := 0
	for _, line := range lines {
		id, _ := getId(line)
		allIdSum += id
		subsets := strings.Replace(line, line[0:strings.Index(line, ":")+1], "", -1)
		subsetsList := strings.Split(subsets, ";")
		for _, subset := range subsetsList {
			colors := getEmptyMapWithColors()
			isValid := a(subset, colors)
			if isValid == false {
				id, _ := getId(line)
				listId = append(listId, id)
				break
			}
		}
	}

	wrongIdSum := 0
	for _, lid := range listId {
		wrongIdSum += lid
	}

	return utils.ToString(allIdSum - wrongIdSum)
}

func second(lines []string) string {
	result := 0
	resIn := 0
	for _, line := range lines {
		cubes := maxNumberOfCubes()
		subsets := strings.Replace(line, line[0:strings.Index(line, ":")+1], "", -1)
		subsetsList := strings.Split(subsets, ";")
		for _, subset := range subsetsList {
			resIn = b(subset, cubes)
		}

		result += resIn
	}

	return utils.ToString(result)
}

func main() {
	lines := utils.ReadLines("input/day02.txt")
	println(first(lines))
	println(second(lines))
}
