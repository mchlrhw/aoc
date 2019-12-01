pub fn calculate_fuel(mass: u32) -> u32 {
    (mass / 3).checked_sub(2).unwrap_or(0)
}

pub fn calculate_fuel_inclusive(mass: u32) -> u32 {
    let mut fuel = calculate_fuel(mass);

    if fuel > 0 {
        fuel += calculate_fuel_inclusive(fuel);
    }

    fuel
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest_parametrize;
    use std::include_bytes;

    #[rstest_parametrize(
        mass,
        expected,
        case(12, 2),
        case(14, 2),
        case(1969, 654),
        case(100756, 33583)
    )]
    fn fuel_calculation_examples(mass: u32, expected: u32) {
        assert_eq!(calculate_fuel(mass), expected)
    }

    #[test]
    fn part_1_solution() -> Result<(), std::num::ParseIntError> {
        let puzzle_input = String::from_utf8_lossy(include_bytes!("day_01/input.txt"));

        let mut total = 0;
        for line in puzzle_input.lines() {
            let mass = line.parse::<u32>()?;
            let fuel = calculate_fuel(mass);
            total += fuel;
        }

        assert_eq!(total, 3317100);

        Ok(())
    }

    #[rstest_parametrize(
        mass,
        expected,
        case(12, 2),
        case(14, 2),
        case(1969, 966),
        case(100756, 50346)
    )]
    fn fuel_calculation_inclusive_examples(mass: u32, expected: u32) {
        assert_eq!(calculate_fuel_inclusive(mass), expected)
    }

    #[test]
    fn part_2_solution() -> Result<(), std::num::ParseIntError> {
        let puzzle_input = String::from_utf8_lossy(include_bytes!("day_01/input.txt"));

        let mut total = 0;
        for line in puzzle_input.lines() {
            let mass = line.parse::<u32>()?;
            let fuel = calculate_fuel_inclusive(mass);
            total += fuel;
        }

        assert_eq!(total, 4972784);

        Ok(())
    }
}
